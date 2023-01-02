import cv2
from moviepy.editor import VideoFileClip
from rembg import remove
from PIL import Image
import glob
import numpy as np

# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture("/home/python/project/website/python_funcs/20230102_120604.mp4")
# videoClip = VideoFileClip("/home/python/project/django/kambiz/python_funcs/tyser.mp4")
# videoClip.write_gif("my-life.gif")
success, image = cap.read()
x,y,h = image.shape
frame_count = 0
step =10
counter = step
# cv2.imshow("ali",image)
while success:
    if frame_count == counter :
        # image = cv2.rotate(image,cv2.ROTATE_180)
        outimage = remove(image)
        cv2.imwrite(f"extracted_images/{int(frame_count/step)}.jpg", outimage)
        counter += step
    success, image = cap.read()
    frame_count += 1
    
cap.release()



frameSize = (int(y),int(x))
# img_bg = np.zeros((y,x,3),np.uint8)
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, frameSize)

for filename in glob.glob("extracted_images/*.jpg"):
    img = cv2.imread(filename)
    out.write(img)

out.release()
