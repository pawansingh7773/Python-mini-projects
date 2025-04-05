import cv2



hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'hand.xml')

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands
    hands = hand_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Hand Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
