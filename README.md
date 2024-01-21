# Hand Volume Control Application

## Overview

The "Volume_Controller.py" Python application is an advanced tool designed to provide a seamless system volume control experience through hand gestures. By harnessing cutting-edge technologies like PyQt5, OpenCV, Mediapipe, and PyAutoGUI, this application transforms your webcam into an intuitive interface for adjusting the volume.

## Features

- **Real-time Hand Gesture Detection:** Leveraging the power of Mediapipe, the application accurately tracks hand landmarks in real-time, enabling a natural and responsive volume control experience.

- **Responsive User Interface:** The PyQt5 framework contributes to an elegant and user-friendly interface, elevating the overall user experience. The interface displays the webcam feed with overlay visuals for hand landmarks.

- **Dynamic Volume Adjustment:** Through the intelligent analysis of the distance between key landmarks on the detected hand, the application dynamically adjusts the system volume. Move your hand up to increase the volume and down to decrease it, providing an intuitive control mechanism.

- **Cross-Platform Compatibility:** With portability in mind, the application is designed to be compatible with various platforms, ensuring a consistent and reliable experience regardless of the operating system.

## Installation

To run the application, install the required libraries using the following command:

**pip install PyQt5 opencv-python mediapipe pyautogui**

## How to Run

Experience the **Hand Volume Control App** and effortlessly control your system volume using intuitive hand gestures. Follow these simple steps to get started:

1. **Clone the Repository:**

   **git clone https://github.com/anandgit01/Volume_Controller.git**
   
2. **Navigate to the Application Directory:**
   
   **cd Volume_Controller**

3. **Run the Application:**
  
    **python Volume_Controller.py**
   
The application window will swiftly open, presenting the webcam feed with intuitive hand gesture controls for adjusting the system volume.
## Libraries Used

- **PyQt5**
PyQt5 offers a robust set of Python bindings for the Qt application framework, empowering the creation of sophisticated graphical user interfaces.

- **OpenCV (cv2)**
OpenCV stands as a powerful open-source computer vision and machine learning library extensively utilized for image and video processing.

- **Mediapipe**
Mediapipe presents a comprehensive library for constructing perception pipelines, making it particularly well-suited for applications requiring real-time hand tracking.

- **PyAutoGUI**
PyAutoGUI facilitates cross-platform GUI automation, allowing for programmatically controlling mouse and keyboard inputs.

## Notes
Ensure that your webcam is properly connected and accessible by the application.
The application employs the PyAutoGUI library to simulate key presses for volume control.
## Author
**Anand Mathew (GitHub: anandgit01)**
