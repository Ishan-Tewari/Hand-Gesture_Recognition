# Hand-Gesture_Recognition
Communication between people comes from various tangible modes like motion, discourse, facial and body articulations. The primary benefit of utilizing hand motions is to cooperate with computer as a non-contact human computer input methodology. The condition of craft of human computer connection presents the realities that for controlling the computer measures offers of different sorts of hand developments have been utilized .The current exploration exertion characterizes a climate where a number of difficulties have been considered for getting the hand motion acknowledgment strategies in the virtual climate. Being a fascinating piece of the Human computer cooperation hand motion acknowledgment should be hearty for genuine applications, yet complex design of human hand presents a progression of difficulties for being followed and deciphered. Other than the motion intricacies like fluctuation and adaptability of design of hand different difficulties incorporate the shape of signals, continuous application issues, presence of foundation commotion and varieties in brightening conditions. The specifications also involve accuracy of detection and recognition for real life applications [2].
Thus the problem that we are trying to resolve is to use a hand tracking system in smart home devices so as to perform the various functions of these devices using just the hand gesture. Hand tracking system has its own set of barriers as:

1. The dimension of the input
2. Clarity of the video input
3. Presence of multiple hands
4. Skin texture and color of the hands
5. Associating functions to unique hand gestures

Our project surrounds the topic of volume control using hand gestures and thus the pointers to index finger and thumb is used. These tasks are performed using Image and video processing by manipulating the image as input and locating the object of importance. OpenCV library has been used, thus the BGR images are changed to RGB images and to those images we apply MediaPipe algorithm.

**What is MediaPipe?**

MediaPipe is a framework which runs on cross platforms(i.e Android, iOS, web, edge devices) for building multimodal (eg. video, audio, any time series data applied ML pipelines. It is currently in development by Google. It contains various cutting edge models like:
1. Face Detection
2. Multi-hand Tracking
3. Hair Segmentation
4. Object Detection and Tracking
5. Objectron: 3D Object Detection and Tracking
6. AutoFlip: Automatic video cropping pipeline
Out of this, we use the 2nd one i.e Multi-hand Tracking.

_The details of the code can be read from the uploaded report._

**Implementation Results**

We observed that the volume modulation works pretty well in general scenarios but some of the problems we noticed are as follows:
1. The distance of the hand from the camera is inversely proportional to the accuracy of the change in volume i.e. the further away the hand is from the camera, more difficult it is for the model to predict the change in length accurately.
2. The naive implementation was a bit too sensitive so we reduced the sensitivity with some fine tuning.

