import cv2
import mediapipe as mp
import time                         #to check frame rate

#to capture the video
cap = cv2.VideoCapture(0)

# using mediapipe for getting the hands recognized (21 points called landmarks per hand)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# to draw points and lines on hands
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()

    # converting the image to RGB from BGR
    imageRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    # to check if hand is detected or not, returns NONE if single hand and returns numeric value if multiple hands
    # print(results.multi_hand_landmarks)

    # drawing connections on hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # to print the id of landmarks (points on hand) with their pixel location
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print (id, cx, cy)
                if id == 4:
                    cv2.circle(img,(cx,cy),15,(255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img,handLms, mpHands.HAND_CONNECTIONS)

    # adding fps to the image
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,3,(255,0,255),3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)