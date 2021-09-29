import cv2 as CV2

for i in range(1,25):

    imagePath = f"./Triangles/{i}.jpg"
    imageRaw = CV2.imread(imagePath)

    width, height = 100, 100
    imageResized = CV2.resize(imageRaw, (width, height))

    imageName = f"{i}.jpg"
    status = CV2.imwrite(imageName, imageResized)
    

# x1, x2 = 1, 295
# y1, y2 = 1, 296

# imageCropped = imageRaw[y1:y2, x1:x2]

# width, height = 100, 100
# imageResized = CV2.resize(imageCropped, (width, height))

# CV2.imshow("1", imageResized)
# CV2.imshow("2", imageResized)
# CV2.waitKey(0)