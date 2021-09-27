import cv2 as CV2

from PIL import Image
# img = Image.open('image.png').convert('L')
# img.save('greyscale.png')

path = "./Circles/23.jpg"
# img = CV2.imread(path)
img = Image.open(path).convert('L')
imgFlatten = img.flatten()

# imgResized = CV2.resize(img, (20, 20))

# imgFlatten = imgResized.flatten()
# print(imgFlatten.size)

# i = 0

# for i in imgResized:
#     print(i)

# for e in imgFlatten:
#     if e < 250:
#         i += 1
#         print(i, e)