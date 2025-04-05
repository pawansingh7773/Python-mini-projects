from cvzone.HandTrackingModule
import (HandDetector)
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7, maxHands=1)

while True:
    success, img = cap.read()
    if not success:
        print("Error: Unable to access webcam.")
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)
    cv2.imshow("Hand Tracking Test", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Esc key exits
        break

cap.release()
cv2.destroyAllWindows()
