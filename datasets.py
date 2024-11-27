from pathlib import Path
import cv2


class ImagesDataset:
	def __init__(self, images_folder=None):
		self.len = 0
		self.set = []

	def add(self, image_path):
		pass

	def add_folder(self):
		pass

	def add_image(self, image_path):
		self.set.append(image_path)

	def __len__(self):
		return len(self.set)

	def __getitem__(self, index):
		image = cv2.imread(self.set[index])
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		return image



