from rembg import remove
from PIL import Image
import cv2
import glob

output_path = '/home/python/project/website/python_funcs/3/out/out{}.png'
s = 1
for filename in glob.glob('/home/python/project/website/python_funcs/3/*.JPG'):
    # img = cv2.imread(filename)

    input = Image.open(filename)
    output = remove(input)
    output.save(output_path.format(s))
    s+=1



