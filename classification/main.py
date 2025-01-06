import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=2)

web_camera = cv2.VideoCapture(0)

web_camera.set(3,1280)
web_camera.set(4,720)

num1 = 0
num2 = 0
operation = "+"
result = 0

def draw_operations(frame, operation):
        if operation == "+":
            cv2.putText(frame, "+", (600, 100), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 10)
        elif operation == "-":
            cv2.putText(frame, "-", (600, 100), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 10)
        elif operation == "*":
            cv2.putText(frame, "*", (600, 100), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 10)
        elif operation == "/":
            cv2.putText(frame, "/", (600, 100), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 255), 10)

while True:
    is_camera_ok, frame = web_camera.read()

    if not is_camera_ok:
        print('CAMERA IS NOT WORKING')

    frame = cv2.flip(frame, 1)

    hands, frame = detector.findHands(frame)

    total_fingers_left = 0
    total_fingers_right = 0

    if hands:
        for i, hand in enumerate(hands):
            fingers = detector.fingersUp(hand)
            total_fingers = sum(fingers)

            if i == 0: 
                total_fingers_left = total_fingers
            elif i == 1: 
                total_fingers_right = total_fingers

        if operation:
            cv2.putText(frame, f"Operation: {operation}", (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        if operation == "+":
            result = total_fingers_left + total_fingers_right
        elif operation == "-":
            result = total_fingers_left - total_fingers_right
        elif operation == "*":
            result = total_fingers_left * total_fingers_right
        elif operation == "/":
            if total_fingers_right != 0:
                result = total_fingers_left / total_fingers_right
            else:
                result = "Error (div by 0)"

        cv2.putText(frame, f"Left Hand: {total_fingers_left}", (10, 150), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Right Hand: {total_fingers_right}", (10, 200), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Result: {result}", (10, 250), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        draw_operations(frame, operation)

    cv2.imshow("AI CALC", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('+'):
        operation = "+"
    elif key == ord('-'):
        operation = "-"
    elif key == ord('*'):
        operation = "*"
    elif key == ord('/'):
        operation = "/"

web_camera.release()
cv2.destroyAllWindows()
