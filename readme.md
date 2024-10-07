```commandline
pip install numpy
pip install matplotlib
pip install opencv-python
```

## example
```python
import cv2
from orthostitcher import CV2VideoStitcher

video_path = "../renders/output.mp4"


stitcher = CV2VideoStitcher(video_path)
frame = stitcher.stitch()

cv2.imwrite("image.png", frame)
```
https://stackoverflow.com/questions/34362922/how-to-use-opencv-stitcher-class-with-python