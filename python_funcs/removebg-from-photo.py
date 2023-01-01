from rembg import remove
from PIL import Image

input_path = ['IMG_1539.JPG','IMG_1543.JPG','IMG_1565.JPG','IMG_1592.JPG']
output_path = '/home/python/project/website/python_funcs/out{}.png'
s = 1
for i in input_path:
    input = Image.open(i)
    output = remove(input)
    output.save(output_path.format(s))
    s+=1