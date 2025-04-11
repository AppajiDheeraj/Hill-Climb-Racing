# 🏁 Hill Climbing Race Controller (Hand Gesture Based)

Control the gas and brake of your favorite hill climbing game using just your hand gestures!  
This real-time hand gesture-based controller uses **MediaPipe** and **OpenCV** to detect open/closed hand states and triggers keyboard inputs accordingly via **PyAutoGUI**.

---

## 📸 Demo
<br>

---

## 🎮 Game Controls (Hill Climb Racing)

| Gesture        | Action Triggered |
|----------------|------------------|
| ✋ All Fingers Open | Accelerate (Gas Pedal) |
| ✊ Fist (All Fingers Closed) | Brake (Reverse) |

---

## 🧠 How It Works

- Uses **MediaPipe Hands** to detect hand landmarks.
- Detects whether fingers are open or closed based on relative positions.
- Maps:
  - Open hand → `Right Arrow` key (gas)
  - Closed fist → `Left Arrow` key (brake)
- Visual feedback is provided on the video feed with clear UI labels.

---

## 🛠️ Built With

- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands)
- [OpenCV](https://opencv.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)

---

## 🧪 Run the Project

1. Clone the repository or copy the script.
2. Install the dependencies:

   ```bash
   pip install opencv-python mediapipe pyautogui
   ```
3. Run the script:
   
    ```bash
    python hill_climb_gesture_controller.py
    ```
4. Open Hill Climb Racing (or similar game that uses arrow keys) and control it with your hand gestures!
5. Press q to quit.

---

## 📸 Screenshots

| GAS Gesture (Hand Open)            | BRAKE Gesture (Fist Closed)         |
|------------------------------------|-------------------------------------|
| ![Gas Gesture](path/to/gas_image)  | ![Brake Gesture](path/to/brake_image) |

---
## ⚠️ Notes
- Make sure your webcam is on and your hand is visible in the frame.

- Works best with proper lighting and a clean background.

- Adjust detection thresholds if needed for your environment.

---

## 🙌 Credits
Created with ❤️ using:

- MediaPipe Hands

- OpenCV

- PyAutoGUI
