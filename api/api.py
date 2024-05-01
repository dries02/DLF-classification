from tensorflow import keras
import cv2
import numpy as np
from fastapi import FastAPI, UploadFile


# Sorted alphanumerically...
_PLANT_NAMES = [
    "Ulmus carpinifolia",  # 1
    "Sorbus aucuparia",  # 10
    "Salix sinerea",  # 11
    "Populus",  # 12
    "Tilia",  # 13
    "Sorbus intermedia",  # 14
    "Fagus silvatica",  # 15
    "Acer",  # 2
    "Salix aurita",  # 3
    "Quercus",  # 4
    "Alnus incana",  # 5
    "Betula pubescens",  # 6
    "Salix alba 'Sericea'",  # 7
    "Populus tremula",  # 8
    "Ulmus glabra"  # 9
]

app = FastAPI()
model = keras.models.load_model('../models/model.keras')


def get_topk_classes(probabilities: list[float], k: int) -> tuple[list[float], list[int]]:
    """
    Get the indices of the top k most likely predictions.
    :param probabilities: the probability distribution corresponding to the classes.
    :param k: the number of classes to predict.
    :return: the tuple of the top k classes with their probabilities.
    """
    zipped_probs = list(zip(probabilities, range(len(probabilities))))
    zipped_probs.sort(key=lambda x: x[0], reverse=True)
    top5 = zipped_probs[:k]
    return zip(*top5)


def convert_image(file: UploadFile) -> np.ndarray:
    """
    Convert the input file to something that the model can make a prediction on.
    :param file: the file as uploaded by the user, containing byte code.
    :return: a numerical RGB matrix representing the 8-bit image.
    """
    img_bytes = file.file.read()
    decoded_img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), -1)
    decoded_img = cv2.resize(decoded_img, (128, 128))
    return np.expand_dims(decoded_img, axis=0)


@app.post('/predict',
          summary='Takes an image of a Swedish leaf and uses a Convolutional Neural Network to predict its species.',
          response_description='The top 3 most likely leaf species and the epistemic uncertainty.'
          )
def predict(file: UploadFile):
    input_image_arr = convert_image(file)
    predictions = model.predict(input_image_arr)[0]
    probs, classes = get_topk_classes(predictions, k=3)
    predicted_plants = [_PLANT_NAMES[plant_idx] for plant_idx in classes]
    confidence = [f'{prob:.3f}' for prob in probs]
    return {'classes': predicted_plants, 'confidence': confidence}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)
