from PIL import Image
import numpy as np
import os
import pandas as pd
import cv2 as cv
from sklearn.utils import shuffle


class Preprocessor:
	@staticmethod
	def load_images() -> pd.DataFrame:
		data = []
		for directory in os.listdir('../data/'):
			label = int(directory[4:]) - 1
			for imagepath in os.listdir('../data/' + directory):
				image = Image.open(os.path.join('../data/', directory + '/' + imagepath))
				new_image = np.array(cv.resize(np.asarray(image), (128, 128)))
				data.append((new_image, label))
				# data.append(((cv.resize(np.asarray(image),(64,64)).flatten() / 255).astype('float32'), label))
				image.close()
		df = shuffle(pd.DataFrame(data, columns=['images', 'labels']))
		return df
