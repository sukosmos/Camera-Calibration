import numpy as np
import cv2 as cv
import os

video_path = r'C:\Users\user\Documents\25-1\컴비\codes\Camera-Calibration\checkerboard.mp4'
calib_file = 'calibration_result.npz'

assert os.path.exists(calib_file), "Calibration result not found! Run camera_calibration.py first."

# Load calibration data
data = np.load(calib_file)
K = data['K']
dist_coeff = data['dist']

# Open video
video = cv.VideoCapture(video_path)
assert video.isOpened(), "Cannot open video: " + video_path

show_rectify = True
map1, map2 = None, None

while True:
    valid, img = video.read()
    if not valid:
        break

    info = "Original"
    if show_rectify:
        if map1 is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
        img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
        info = "Rectified"

    cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
    cv.imshow("Geometric Distortion Correction", img)

    key = cv.waitKey(10)
    if key == 27:        # ESC
        break
    elif key == ord('\t'):  # Tab
        show_rectify = not show_rectify
    elif key == ord(' '):   # Space to pause
        cv.waitKey()

video.release()
cv.destroyAllWindows()
