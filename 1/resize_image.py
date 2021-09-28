import cv2 as CV2

# CV2.imshow("circle", imgResized)
# CV2.waitKey(0)

# circleImages = [3,5,11,12,15,17,18,20,21,24]
# triangleImages = [3,4,5,8,9,12,13,14,16,17,19,20]
# rectangleImages = [5,12,16,17]

# for c in circleImages:
#     path = f"./Circles/{c}.jpg"
#     img = CV2.imread(path)

#     x1, x2 = 1, 149
#     y1, y2 = 1, 149

#     imgCropped = img[y1:y2, x1:x2]
#     imgResized = CV2.resize(imgCropped, (150, 150))

#     imgName = f"{c}.jpg"
#     CV2.imwrite(imgName, imgResized)


# imageNumber = 24
# imagePath = f"./Triangles/{imageNumber}.jpg"
# imageRaw = CV2.imread(imagePath)


# CV2.imshow("1", imageRaw)
# # CV2.imshow("2", imageResized)
# CV2.waitKey(0)

# x1, x2 = 7, 98
# y1, y2 = 2, 98

# imageCropped = imageRaw[y1:y2, x1:x2]

# width, height = 150, 150
# imageResized = CV2.resize(imageCropped, (width, height))

# imageName = f"{imageNumber}.jpg"
# status = CV2.imwrite(imageName, imageResized)


# CV2.imshow("1", imageResized)
# CV2.imshow("2", imageResized)
# CV2.waitKey(0)