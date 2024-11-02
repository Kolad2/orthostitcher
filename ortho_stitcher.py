import numpy as np
import cv2
import os

class VideoFrameGetter:
	def __init__(self, path):
		# Открываем видеофайл
		self.video = cv2.VideoCapture(path)
		self.frame_count = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

	def get(self, num):
		self.video.set(cv2.CAP_PROP_POS_FRAMES, num)
		ret, frame = self.video.read()
		return frame

	def get_frame_set(self, start_frame=None, end_frame=None):
		start_frame = start_frame if start_frame is not None else 0
		end_frame = end_frame if end_frame is not None else self.frame_count
		return [self.get(num) for num in range(start_frame, end_frame)]

	def __del__(self):
		self.video.release()


class ImagesFolderGetter:
	def __init__(self, path_to_folder):
		"""
		Инициализирует объект ImageFolderGetter.

		:param path_to_folder: Путь к папке с изображениями
		"""
		self.path = path_to_folder
		self.image_files = self._get_image_files()
		self.frame_count = len(self.image_files)

	def _get_image_files(self):
		"""
		Получает и сортирует список файлов изображений в папке.

		:return: Отсортированный список путей к изображениям
		"""
		supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')
		files = [
			os.path.join(self.path, file)
			for file in os.listdir(self.path)
			if file.lower().endswith(supported_extensions)
		]
		files.sort()  # Сортируем файлы по имени
		return files

	def get(self, num):
		"""
		Возвращает изображение по номеру кадра.

		:param num: Номер кадра (индекс)
		:return: Изображение в формате NumPy массива
		:raises IndexError: Если номер кадра вне диапазона
		:raises IOError: Если не удалось загрузить изображение
		"""
		if num < 0 or num >= self.frame_count:
			raise IndexError("Номер кадра вне допустимого диапазона")

		image_path = self.image_files[num]
		frame = cv2.imread(image_path)

		if frame is None:
			raise IOError(f"Не удалось загрузить изображение: {image_path}")

		return frame

	def get_frame_set(self, start_frame=None, end_frame=None):
		"""
		Возвращает набор кадров от start_frame до end_frame.

		:param start_frame: Начальный кадр (по умолчанию 0)
		:param end_frame: Конечный кадр (по умолчанию последний кадр)
		:return: Список изображений
		"""
		start_frame = start_frame if start_frame is not None else 0
		end_frame = end_frame if end_frame is not None else self.frame_count
		return [self.get(num) for num in range(start_frame, end_frame)]


class CV2VideoStitcher:
	def __init__(self, path_to_video=None, path_to_folder=None, start_frame=None, end_frame=None):
		if path_to_video is not None:
			image_set = VideoFrameGetter(path_to_video)
			self.frame_count = image_set.frame_count
			self.frames = self.video.get_frame_set(start_frame, end_frame)

		if path_to_folder is not None:
			image_set = ImagesFolderGetter(path_to_folder)
			self.frames = image_set.get_frame_set(start_frame, end_frame)

		self.stitcher = cv2.Stitcher.create(cv2.Stitcher_SCANS)

	def stitch(self):
		(_result, frame_result) = self.stitcher.stitch(self.frames)
		return frame_result
