import cv2 as CV2

# imgPath = "./image2.jpg"
# imgRaw = CV2.imread(imgPath)
# imgResized = CV2.resize(imgRaw, (300, 500))
# imgCropped = imgResized[1:500, 1:300]

# x1, x2 = 0, 100
# y1, y2 = 0, 100
# imgCount = 1

# while True:
#     imgCropped2 = imgCropped[y1:y2, x1:x2]
#     imgName = f'{imgCount}.jpg'
#     status = CV2.imwrite(imgName, imgCropped2)

#     if x1 == 200 and x2 == 300 and y1 == 400 and y2 == 500:
#         break 

#     if x2 != 300:
#         x1, x2 = x2, x2 + 100
#     else:
#         x1, x2 = 0, 100
#         y1, y2 = y1 + 100, y2 + 100

#     imgCount += 1

# imgPath = "./Triangle.jpg"
# imgRaw = CV2.imread(imgPath)

# width, height = 400, 600
# imgResized = CV2.resize(imgRaw, (width, height))

# x1, x2 = 0, 100
# y1, y2 = 0, 100
# imgCount = 1

# while True:
#     imgCropped = imgResized[y1:y2, x1:x2]
#     imgName = f'{imgCount}.jpg'
#     status = CV2.imwrite(imgName, imgCropped)

#     if x1 == 300 and x2 == 400 and y1 == 500 and y2 == 600:
#         break 

#     if x2 != 400:
#         x1, x2 = x2, x2 + 100
#     else:
#         x1, x2 = 0, 100
#         y1, y2 = y1 + 100, y2 + 100

#     imgCount += 1

# CV2.imshow("circle", imgResized)
# CV2.waitKey(0)








imageNumber = 24
imagePath = f"./Triangles/{imageNumber}.jpg"
imageRaw = CV2.imread(imagePath)


# CV2.imshow("1", imageRaw)
# # CV2.imshow("2", imageResized)
# CV2.waitKey(0)

x1, x2 = 7, 98
y1, y2 = 2, 98

imageCropped = imageRaw[y1:y2, x1:x2]

width, height = 150, 150
imageResized = CV2.resize(imageCropped, (width, height))

imageName = f"{imageNumber}.jpg"
status = CV2.imwrite(imageName, imageResized)


# CV2.imshow("1", imageResized)
# CV2.imshow("2", imageResized)
# CV2.waitKey(0)