# Camera-Calibration
Camera calibration using OpenCV

<br><br>

## camera_calibration.py

Detects **chessboard corners** in a video
Performs camera calibration to get the camera matrix & distortion coefficients.

- Frame Selection
    
    ```python
    if select_all:
        complete, _ = cv.findChessboardCorners(img, board_pattern)
        if complete:
            selected.append(img)
    ```
    
    Automatically selects frames with a detectable chessboard pattern
    

- camera calibration
    
    ```python
    rms, K, dist_coeff, rvecs, tvecs = cv.calibrateCamera(obj_points, img_points, gray_shape, K, dist_coeff, flags=calib_flags)
    ```
    
    Estimates the camera matrix and distortion coefficients using the selected frames.
    

- Save calibration result
    
    ```python
    np.savez('calibration_result.npz', K=K, dist=dist_coeff)
    ```
    
    Saves the calibration result to a `.npz` file to be used for distortion correction.
    

### Calibration Result

```
## Camera Calibration Results
* The number of selected images = 305
* RMS error = 1.001489
* fx = 970.425123, fy = 966.596836
* cx = 544.049793, cy = 956.938051
* Camera matrix (K):
[[970.42512263   0.         544.04979348]
 [  0.         966.59683583 956.93805147]
 [  0.           0.           1.        ]]
* Distortion coefficients (k1, k2, p1, p2, k3, ...) =
[ 0.03566128 -0.03956261 -0.00058778  0.00177353  0.01540355]
```

## distortion_correction.py

Reads the calibration result and corrects lens distortion in the original video.

- **Apply Distortion Correction**
    
    ```python
    map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
    img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
    ```
    
    Undistorts each video frame using the calibration data.
    
- Toggle between original and corrected view
    
    ```python
    if key == ord('\t'):
        show_rectify = not show_rectify
    ```
    
    Toggle between original and corrected view using the `TAB` key during playback.
    

### Result

<p align="center">
  <img src = "https://github.com/user-attachments/assets/4570073f-0a66-43fe-b436-fb792705ef32" width="40%" height="40%">  
  <img src = "https://github.com/user-attachments/assets/d2febf1f-c3bc-410f-bf1c-187022d0e89d" width="40%" height="40%">
</p>

---

*For Computer Vision*
