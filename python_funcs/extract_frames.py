import cv2
from moviepy.editor import VideoFileClip
from rembg import remove
from PIL import Image

# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture("/home/python/project/website/python_funcs/hadi.mp4")
# videoClip = VideoFileClip("/home/python/project/django/kambiz/python_funcs/tyser.mp4")
# videoClip.write_gif("my-life.gif")

success, image = cap.read()
frame_count = 0
counter =10
# cv2.imshow("ali",image)
while success:
    if frame_count == counter :
        image = cv2.rotate(image,cv2.ROTATE_180)
        outimage = remove(image)
        cv2.imwrite(f"extracted_images/frame_{int(frame_count/10)}.jpg", outimage)
        counter += 10
    success, image = cap.read()
    frame_count += 1
    
cap.release()
