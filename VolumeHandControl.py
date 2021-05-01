import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


#################################
# height and widht of capture
wCam, hCam = 640, 480
#################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
volBar = 0
volPer = 0
volPrev = 0
count = 0
vol = 0
marker = True

while marker:
    success, img = cap.read()
    volPrev = vol
    # finding location of hands
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    if len(lmList) != 0:
        # 4 for thumb and 8 for index finger
        # print(lmList[4], lmList[8])

        # highlighting index finger tip. thumb tip, line between them and the center of the line in the image
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx,cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1,y1), 10, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255, 0, 255), 2)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        # calculating length of the line
        length = math.hypot(x2-x1, y2-y1)
        #print("Length of the line =",length)

        # converting hand length range to volume range
        # Hand length range 50 - 300
        # Volume range -65 - 0
        vol = np.interp(length,[50,200],[minVol,maxVol])
        volBar = np.interp(length, [50, 200], [400, 150])
        volPer = np.interp(length, [50,200], [0,100])

        print("Length of the line is\033[1m",int(length),"\033[0mand the volume is\033[1m",  vol,"\033[0m")
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50,150), (85,400), (102,0,0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255,0,0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40,450), cv2.FONT_ITALIC, 1, (250,0,0), 3)

    # adding fps to the image
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS: " + str(int(fps)), (10, 50), cv2.FONT_ITALIC, 1, (102, 0,0), 2)

    validMin = volPrev-3
    validMax = volPrev+3

    if vol >= validMin and vol <= validMax:
        count += 1
    else:
        count = 0

    if count > 50:
        marker = False
    else:
        cv2.imshow("Img",img)
        cv2.waitKey(1)