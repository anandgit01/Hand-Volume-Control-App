import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt, QTimer
import cv2
import mediapipe as mp
import pyautogui

class HandVolumeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.my_hands, self.mp_drawing = self.initialize_hands()
        self.webcam = cv2.VideoCapture(0)

        self.init_ui()

    def initialize_hands(self):
        return mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5), mp.solutions.drawing_utils

    def detect_hands(self, image):
        output = self.my_hands.process(image)
        return output.multi_hand_landmarks

    def draw_landmarks(self, image, hand_landmarks):
        self.mp_drawing.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    def calculate_distance(self, x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def control_volume(self, dist):
        if dist > 50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    def init_ui(self):
        self.setWindowTitle('Hand Volume Control App')

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def update_frame(self):
        _, frame = self.webcam.read()
        frame = cv2.flip(frame, 1)  # Flip horizontally for a more natural viewing

        hands = self.detect_hands(frame)

        if hands:
            for hand in hands:
                self.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                x1, y1 = int(landmarks[8].x * frame.shape[1]), int(landmarks[8].y * frame.shape[0])
                x2, y2 = int(landmarks[4].x * frame.shape[1]), int(landmarks[4].y * frame.shape[0])
                dist = self.calculate_distance(x1, y1, x2, y2)

                for id, lm in enumerate(landmarks):
                    x = int(lm.x * frame.shape[1])
                    y = int(lm.y * frame.shape[0])
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)

                cv2.line(img=frame, pt1=(x1, y1), pt2=(x2, y2), color=(0, 0, 255), thickness=5)

                self.control_volume(dist)

        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image.rgbSwapped())  # Swap red and blue channels
        self.video_label.setPixmap(pixmap)

    def closeEvent(self, event):
        self.webcam.release()
        super().closeEvent(event)

def main():
    app = QApplication(sys.argv)
    window = HandVolumeApp()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
