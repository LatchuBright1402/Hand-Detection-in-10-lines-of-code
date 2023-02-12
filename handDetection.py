import cv2
import mediapipe
import cvzone

from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    cv2.imshow("image", img)
    cv2.waitKey(1)

