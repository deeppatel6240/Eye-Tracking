# simple Eye Tracking project

we propose an efficient approach for real-time eye-gaze detection from images acquired from a web camera. The measured data is sufficient to describe the eye movement, because the web camera is stationary with respect to the head. First, the image is binarized with a dynamic threshold. Then geometry features of the eye image are extracted from binary image. Next using estimation method based on geometry structure of eye, we detect the positions of two eye corners. After that, the center of iris is detected by matching between an iris boundary model and image contours. Finally, using the relative position information between the center of iris and the eye corners, base on the relationship between image coordinate and monitor coordinate, the position where the eye is looking at the monitor is calculated. This system requires only a low cost web camera and a personal computer. Experimental results show that the proposed system can detect accurately eye movements in realtime.

It makes use of machine learning-based facial mapping (landmarks) with dlib + python + openCV, with eyes projection on a virtual keyboard. 
The algorithm works in real-time on the video-stream from the webcam. 

Video example https://www.youtube.com/watch?v=_vMNbsJFbqM 

--------------------------------------------------------------------------------------------

Logic flow:

- find face and track the right eye;
- calibrate the proper range of allowed space for (comfortable) movement;

(then, frame by frame)

- track the right eye and project its centroid on a virtual keyboard in a "working window";
- take inputs and, specifically, "press" the key, using blinking detection;
- updtate a text string and print on screen (and, by just adding a couple of line, on a file).

--------------------------------------------------------------------------------------------

Requirements: 
- python3
- opencv
- numpy
- dlib (and the trained model shape_predictor_68_face_landmarks.dat; see below)
--------------------------------------------------------------------------------------------

More useful information about Facial mapping (landmarks) with Dlib + python can be found here:
https://towardsdatascience.com/facial-mapping-landmarks-with-dlib-python-160abcf7d672
https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/

The trained model file shape_predictor_68_face_landmarks.dat can be found here:
https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2

