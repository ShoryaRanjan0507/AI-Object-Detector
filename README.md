# AI-Object-Detector
A lightweight Computer Vision application using Deep Learning to identify daily objects and announce them via Text-to-Speech for visually impaired users.

AI Object Detector is a real-time object detection system designed to assist visually impaired individuals in identifying daily objects. Built using **Python**, **YOLOv8**, and **OpenCV**, this project acts as an Intelligent Agent that perceives the environment through a webcam and communicates findings via Text-to-Speech (TTS).


## Key Features
- **Real-time Detection:** Utilizes the YOLOv8-Nano model for high-speed inference on standard laptops.
- **Audio Feedback:** Converts visual labels into spoken words using the `pyttsx3` engine.
- **Smart Filtering:** Implements a confidence threshold (0.6+) to reduce false positives misidentifications.
- **Privacy-First:** All processing happens locally on the device; no camera data is sent to the cloud.


## Tech Stack & Concepts
- **Language:** Python 3.10+
- **Deep Learning Framework:** Ultralytics YOLOv8
- **Computer Vision:** OpenCV
- **Audio Engine:** Pyttsx3
- **AI Concepts Applied:** Supervised Learning, Image Classification, Intelligent Agents, PEAS and Transfer Learning.


## Setup & Installation

### 1. Prerequisite: VS Code Extensions
To run this project efficiently in **VS Code**, ensure you have the following extensions installed:
1. Open **VS Code**.
2. Click on the **Extensions** icon on the left sidebar (or press `Ctrl+Shift+X`).
3. Search for and install:
   * **Python** (by Microsoft): Provides IntelliSense and debugging.
   * **Pylance**: For performant language support.
   * **Jupyter** (Optional): If you wish to run the code in cells.

### 2. Clone and Install Libraries
Open your terminal in VS Code and run the following commands:

# Install the required Python libraries
pip install ultralytics opencv-python pyttsx3
open command prompt and copy paste the above command there or simply copy paste in the VS Code terminal
