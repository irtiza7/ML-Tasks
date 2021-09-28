import cv2 as CV2

imgPath = "./Rectangle.jpg"
imgRaw = CV2.imread(imgPath)

height, width = 1800, 1200
imgResized = CV2.resize(imgRaw, (width, height))

imgCount = 1
x1, x2 = 0, 300
y1, y2 = 0, 300

while True:

    imgCropped = imgResized[y1:y2, x1:x2]
    imgName = f'{imgCount}.jpg'
    status = CV2.imwrite(imgName, imgCropped)

    if x1 == 900 and x2 == 1200 and y1 == 1500 and y2 == 1800:
        break 

    if x2 != 1200:
        x1, x2 = x2, x2 + 300
    else:
        x1, x2 = 0, 300
        y1, y2 = y1 + 300, y2 + 300

    imgCount += 1