import cv2 as cv
import mediapipe as mp
import pyautogui

# Setup MediaPipe
mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Video Capture
video = cv.VideoCapture(0)

while True:
    success, image = video.read()
    image = cv.flip(image, 1)
    img_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    image = cv.cvtColor(img_rgb, cv.COLOR_RGB2BGR)

    h, w, _ = image.shape
    fingers_open = 0

    # Header
    cv.rectangle(image, (0, 0), (640, 70), (0, 0, 0), -1)
    cv.putText(image, "HILL CLIMBING RACE", (70, 50), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)

        lm = hand.landmark

        # Simplified logic:
        # Check if index, middle, ring, and pinky tips are above their lower joints
        # This roughly means they are "open"
        if (
            lm[8].y < lm[6].y and  # Index
            lm[12].y < lm[10].y and  # Middle
            lm[16].y < lm[14].y and  # Ring
            lm[20].y < lm[18].y      # Pinky
        ):
            fingers_open = 5  # All fingers open (thumb assumed open too)
        else:
            fingers_open = 0  # Closed fist

        if fingers_open == 5:
            cv.rectangle(image, (200, 350), (450, 450), (50, 50, 255), -1)
            cv.putText(image, "GAS", (260, 420), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')
        else:
            cv.rectangle(image, (200, 350), (450, 450), (50, 50, 255), -1)
            cv.putText(image, "BRAKE", (230, 420), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')

    else:
        pyautogui.keyUp('right')
        pyautogui.keyUp('left')

    # Show frame
    cv.imshow("Hill Climbing Race", image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()