import cv2 as CV2

imagePath = []

for count in range(1, 25):
    imagePath.append(f"./Circles/{count}.jpg")

for count in range(1, 25):
    imagePath.append(f"./Rectangles/{count}.jpg")

for count in range(1, 25):
    imagePath.append(f"./Triangles/{count}.jpg")


for path in imagePath:

    imageRaw = CV2.imread(path, 0)
    imageResized = CV2.resize(imageRaw, (30, 30))
    imageFlattened = imageResized.flatten()

    temp = []

    for pixel in imageFlattened:
        if pixel < 250:
            temp.append(1)
        else:
            temp.append(0)

    print(temp)


