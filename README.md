# ID Year Detection Project

## Overview
This project utilizes computer vision and audio processing to detect specific colors in real-time using a webcam. When a color is detected, the application highlights the area containing that color in the video feed and provides an auditory output of the detected color.

## Objectives
- **Real-time Color Detection**: Capture video frames from a webcam and convert them to the HSV color space for effective color detection.
- **Bounding Box Visualization**: Draw bounding boxes around detected colors to visually indicate their locations in the video feed.
- **Audio Feedback**: Use text-to-speech technology to announce the detected color, providing an interactive experience.

## Key Features
1. **Color Range Detection**: The application is capable of detecting multiple colors including yellow, brown, green, and blue.
2. **Bounding Box Highlighting**: When a color is detected, a green rectangle is drawn around the area in the video feed where the color is found.
3. **Text-to-Speech Integration**: Each detected color is announced via a speech synthesis engine, enhancing user interaction.

## Technologies Used
- **OpenCV**: For video capture and image processing.
- **Pillow (PIL)**: For image manipulation and bounding box calculations.
- **NumPy**: For array operations and mask generation.
- **pyttsx3**: For converting text to speech, providing audio feedback.

## Installation

### Prerequisites
Ensure you have Python installed on your machine. 

### Dependencies
Install the required libraries using pip:
```bash
pip install opencv-python pillow numpy pyttsx3
