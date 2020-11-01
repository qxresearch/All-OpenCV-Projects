# Color-Detection-Using-HSV-Colorspace (Detecting blue color in a video) 
A live video in which only blue color is detected

# Requirements
* Python >=3.1
* Python Libraries: `numpy`, `cv2`

# Explanation

1. In this project you have to capture the video first using the primary camera of your system.
2. Then you have read the frames and then convert the frames into HSV (Hue, Separation, Value)
3. You have create the mask of the blue color that you want to extract from the live video by giving high and low range values.
4. Finally you have to perform `bitwise-and` operation on the frame and the mask.
5. Display the video

# Output Video 
[Video](https://github.com/varshakr1298/Color-Detection-Using-HSV-Colorspace/blob/master/BlueColorDetection.mp4) in which blue color is detected
