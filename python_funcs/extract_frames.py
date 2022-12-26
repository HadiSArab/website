import cv2
import time
from moviepy.editor import VideoFileClip


# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture("/home/python/project/django/kambiz/python_funcs/tyser.mp4")
# videoClip = VideoFileClip("/home/python/project/django/kambiz/python_funcs/tyser.mp4")
# videoClip.write_gif("my-life.gif")

success, image = cap.read()
frame_count = 0
counter =10
# cv2.imshow("ali",image)
while success:
    if frame_count == counter :
        cv2.imwrite(f"extracted_images/frame_{int(frame_count/10)}.jpg", image)
        counter += 10
    success, image = cap.read()
    frame_count += 1
    
cap.release()
