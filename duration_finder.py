import os
import cv2
from collections import deque

# Paste the path to the directory containing the video files between the quotes
dir_path = r""

dir_path = dir_path.replace('\\', '/')

duration = 0
queue = deque()

dirs = os.listdir(dir_path)

for dir in dirs:
    queue.append(os.path.join(dir_path, dir))

while queue:
    dir = queue.popleft()
    if os.path.isdir(dir):
        subdirs = os.listdir(dir)
        for subdir in subdirs:
            new_path = os.path.join(dir, subdir)
            queue.append(new_path)
    else:
        if dir.endswith((".mp4", ".mkv", ".avi")):
            cap = cv2.VideoCapture(dir)
            if cap.isOpened():
                fps = cap.get(cv2.CAP_PROP_FPS)
                frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                if fps > 0:
                    duration += frames / fps
                cap.release()

hours = int(duration // 3600)
minutes = int((duration % 3600) // 60)
print(f"Total duration of all videos in the directory is {hours} hours and {minutes} minutes")
