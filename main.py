import numpy as np
import cv2
import matplotlib.pyplot as plt

class FrameGetter:
	def __init__(self, path):
		# Открываем видеофайл
		self.cap = cv2.VideoCapture(path)

	def get(self, num):
		self.cap.set(cv2.CAP_PROP_POS_FRAMES, num)
		ret, frame = self.cap.read()
		return frame

	def __del__(self):
		self.cap.release()


fg = FrameGetter('videos/video1.mp4')


stitcher = cv2.Stitcher.create(cv2.Stitcher_SCANS)
frames = [fg.get(num) for num in range(100,160,10)]
(_result, frame_result) = stitcher.stitch(frames)
if frame_result is not None:
	fig = plt.figure(figsize=(14, 9))
	ax = [fig.add_subplot(1, 1, 1)]
	ax[0].imshow(frame_result)
	plt.show()
	cv2.imwrite("frame2.png",frame_result)

cv2.destroyAllWindows()
