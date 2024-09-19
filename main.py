# import cv2
# from PIL import Image

# from util import get_limits
# # print(cv2.__version__)


# yellow = [0, 255, 255]  # yellow in BGR colorspace
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()

#     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     lowerLimit, upperLimit = get_limits(color=yellow)

#     mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

#     mask_ = Image.fromarray(mask)

#     bbox = mask_.getbbox()

#     if bbox is not None:
#         x1, y1, x2, y2 = bbox

#         frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()

# cv2.destroyAllWindows()

# import cv2
# from PIL import Image
# import numpy as np

# def get_limits(color='yellow'):
#     colors = {
#         'yellow': ([20, 100, 100], [30, 255, 255]),
#         'brown': ([10, 50, 50], [20, 255, 255]),
#         'green': ([40, 50, 50], [80, 255, 255]),
#         'blue': ([100, 50, 50], [140, 255, 255]),
#     }
#     return colors.get(color.lower(), ([0, 0, 0], [0, 0, 0]))

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     colors_to_detect = ['yellow', 'brown', 'green', 'blue']

#     for color in colors_to_detect:
#         lowerLimit, upperLimit = get_limits(color=color)
#         mask = cv2.inRange(hsvImage, np.array(lowerLimit), np.array(upperLimit))

#         mask_ = Image.fromarray(mask)
#         bbox = mask_.getbbox()

#         if bbox is not None:
#             x1, y1, x2, y2 = bbox
#             frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
from PIL import Image
import numpy as np
import pyttsx3

def get_limits(color='yellow'):
    colors = {
         'brown': ([10, 50, 50], [20, 255, 255]),
         'green': ([40, 50, 50], [80, 255, 255]),
        'blue': ([100, 50, 50], [140, 255, 255]),
        'yellow': ([20, 100, 100], [30, 255, 255]),
    }
    return colors.get(color.lower(), ([0, 0, 0], [0, 0, 0]))

def speak_color(color):
    engine = pyttsx3.init()
    engine.say(f"Detected ,,, {color} color")
    engine.runAndWait()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    colors_to_detect = ['yellow', 'brown', 'green', 'blue']

    for color in colors_to_detect:
        lowerLimit, upperLimit = get_limits(color=color)
        mask = cv2.inRange(hsvImage, np.array(lowerLimit), np.array(upperLimit))

        mask_ = Image.fromarray(mask)
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            speak_color(color)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

