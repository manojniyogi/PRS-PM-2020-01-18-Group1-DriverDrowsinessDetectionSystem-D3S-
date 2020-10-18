##
# Run the program with the command at python prompt:
# python detect_drowsiness.py
##

# import the necessary packages
import numpy as np
import playsound
import dlib
import cv2
import time
import imutils
from imutils import face_utils
from imutils.video import VideoStream
from scipy.spatial import distance as dist
from threading import Thread


## To play alarm
def sound_alarm(path):
    playsound.playsound(path)

## Get Aspect Ratio
def getAspectRatio(eye):
    ## calculate euclidean distances of vertical landmarks of eye
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    ## calculate euclidean distance of horizontal landmark of eye
    C = dist.euclidean(eye[0], eye[3])

    ## calculate aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear


## Decide Aspect Ratio threshold to trigger alarm
AR_THRESHOLD = 0.3

## Decide idle frames, to trigger alarm
IDLE_FRAMES_THRESHOLD = 48

## Initialize
COUNTER = 0
ALARM_ON = False

## Invoke
print("Loading Facial Landmark Predictor ..")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('model\shape_predictor_68_face_landmarks.dat')

## Capture facial landmarks of eyes
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

## Start Video Streaming
print("Start Video Streaming ...")
vs = VideoStream().start()
time.sleep(.5)

## Loop over video frames till key press - 'q'
while True:
    frame = vs.read()
    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Color to Grascale to reduce processing 3 colors
    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        ## Capture eyes
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        ## Get aspect ratios of eyes
        leftEAR = getAspectRatio(leftEye)
        rightEAR = getAspectRatio(rightEye)

        ## Get average aspect ratio
        ear = (leftEAR + rightEAR) / 2.0

        ## Get boundaries
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        ## Draw boundaries
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        ## Check to see if aspect ratio falls below threshold
        if ear < AR_THRESHOLD:
            COUNTER += 1
            ## Trigger alarm if eyes are closed for set threshold frames
            if COUNTER >= IDLE_FRAMES_THRESHOLD:
                if not ALARM_ON:
                    ALARM_ON = True
                    # Trigger alarm in a separate thread to ensure uninterrupted image processing
                    t = Thread(target=sound_alarm, args=('alarm.mp3',))
                    t.deamon = True
                    t.start()
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        ## Reset counter, alarm if they are above threshold values
        else:
            COUNTER = 0
            ALARM_ON = False

        ## Show Aspect Ratio
        cv2.putText(frame, "AR Score: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    ## Show frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if key pressed 'q' then exit loop
    if key == ord("q"):
        break

# Cleanup resources
cv2.destroyAllWindows()
vs.stop()
