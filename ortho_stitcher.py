import numpy as np
import cv2

class VideoFrameGetter:
	def __init__(self, path):
		# Открываем видеофайл
		self.video = cv2.VideoCapture(path)
		self.frame_count = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

	def get(self, num):
		self.video.set(cv2.CAP_PROP_POS_FRAMES, num)
		ret, frame = self.video.read()
		return frame

	def __del__(self):
		self.video.release()


class CV2VideoStitcher:
	def __init__(self, path_to_video, start_frame, end_frame):
		video = VideoFrameGetter(path_to_video)
		self.frame_count = video.frame_count
		self.stitcher = cv2.Stitcher.create(cv2.Stitcher_SCANS)
		start_frame = start_frame if start_frame is not None else 0
		end_frame = end_frame if end_frame is not None else self.frame_count
		self.frames = [video.get(num) for num in range(start_frame, end_frame)]


	def stitch(self):
		(_result, frame_result) = self.stitcher.stitch(self.frames)
		return frame_result