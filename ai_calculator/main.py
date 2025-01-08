import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=4)

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

    total_fingers = [0] * 4

    if hands:
        for i, hand in enumerate(hands):
            fingers = detector.fingersUp(hand)
            total_fingers[i] = sum(fingers)

        if operation:
            cv2.putText(frame, f"Operation: {operation}", (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        if operation == "+":
            result = sum(total_fingers)
        elif operation == "-":
            result = total_fingers[0] - total_fingers[1]
        elif operation == "*":
            result = 1
            for fingers in total_fingers:
                result *= fingers
        elif operation == "/":
            if total_fingers[1] != 0:
                result = total_fingers[0] / total_fingers[1]
            else:
                result = "Error (div by 0)"

        for i, fingers in enumerate(total_fingers):
            if i < len(hands):
                cv2.putText(frame, f"Hand {i+1}: {fingers} Fingers", (10, 150 + 50 * i), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(frame, f"Result: {result}", (10, 350), 
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
