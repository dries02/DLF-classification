import cv2
import numpy as np
from PIL import Image
import os
import pandas as pd

class Preprocessor:
	@staticmethod
	def load_images(dir: str, resize_dims: tuple[int, int]) -> pd.DataFrame:
		"""
		:param dir: the directory containing the images
		:param resize_dims: the dimensions to resize the image to
		:return: the loaded dataset
		"""
		data = []
		for directory in os.listdir(dir):
			label = int(directory[4:]) - 1
			for imagepath in os.listdir(dir + directory):
				image = Image.open(os.path.join(dir, directory + '/' + imagepath))
				new_image = cv2.resize(np.array(image), resize_dims)
				data.append((new_image.flatten(), label))
				image.close()
		df = pd.DataFrame(data, columns=['images', 'labels'])
		return df
