import pygetwindow as gw
import numpy as np
import cv2
import time
from mss import mss #mss is a python library for screenshots
from PIL import Image

"""
    screen_recorder.py
    This is a application to record thermal videos on top of the SeekOFix application.
    
    Author: Group from 2021/2022 (Jonathan Mack)
    Edited by Hiu Sum Jaime Yue
"""

# Maximize and bring SeekOFix window to the foreground
seekOFixWindow = gw.getWindowsWithTitle('SeekOFix')[0]
seekOFixWindow.maximize()
seekOFixWindow.activate()

# These depend on host resolution
# 2023: Changes below due to the difference between computer screens dimensions
X_OFFSET = 18 #2023: Might need changes (2022: 17)
Y_OFFSET = 62 #2023: Might need changes (2022: 64)

VIDEO_WIDTH = 618 #2023: Might need changes (2022: 620)
VIDEO_HEIGHT = 432 #2023: Might need changes (2022: 470)

# Monitor for mss (screenshots)
monitor = {'left': X_OFFSET, 'top': Y_OFFSET, 'width': VIDEO_WIDTH, 'height': VIDEO_HEIGHT}

# Resolution for VideoWriter object (video export)
resolution = (VIDEO_WIDTH, VIDEO_HEIGHT)

# MP4 codec
codec = cv2.VideoWriter_fourcc(*'mp4v')

# Timestamped filename
timestamp = time.strftime('%Y.%m.%d-%H.%M.%S')
filename = '{}.mp4'.format(timestamp)
testDataFolder = './Test Data'
videoPath = '{}/{}'.format(testDataFolder, filename)

# Limit image grab rate based on VideoWriter fps
fps = 10.0
counterLimit = (30 / fps)

# Create VideoWriter object
out = cv2.VideoWriter(videoPath, codec, fps, resolution)

# Create empty window
cv2.namedWindow('Live', cv2.WINDOW_NORMAL)

# Resize this window 
cv2.resizeWindow('Live', 480, 270)

# Count number of frames that passed since previous write to video
counter = 0

with mss() as sct:
    while True:
        screenShot = sct.grab(monitor)
        img = Image.frombytes(
            'RGB',
            (screenShot.width, screenShot.height),
            screenShot.rgb,
        )

        frame = np.array(img)

        # Convert from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        counter += 1

        # Write an image to the video every X captures
        if counter >= counterLimit:
            counter = 0
            out.write(frame)

            # Display the recording screen
            cv2.imshow('Live', frame)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):

            # Release the Video writer
            out.release()

            # Destroy all windows
            cv2.destroyAllWindows()
            break
