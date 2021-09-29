import cv2 as CV2
import xlsxwriter as Excel

outWorkbook  = Excel.Workbook("Shapes_Dataset.xlsx")
outSheet = outWorkbook.add_worksheet()

imagePath = []

for count in range(1, 25):
    imagePath.append(f"./Circles/{count}.jpg")

for count in range(1, 25):
    imagePath.append(f"./Rectangles/{count}.jpg")

for count in range(1, 25):
    imagePath.append(f"./Triangles/{count}.jpg")

row, column = 0, 0

for box in range(1, 2502):
    
    heading = f"I_{box}"
    outSheet.write(row, column, heading)
    column += 1

row, column = 1, 0

for path in imagePath:

    imageRaw = CV2.imread(path, 0)
    imageResized = CV2.resize(imageRaw, (50, 50))
    imageFlattened = imageResized.flatten()

    temp = []

    for pixel in imageFlattened:
        if pixel < 230:
            temp.append(1)
        else:
            temp.append(0)

    for element in temp:
        outSheet.write(row, column, element)
        column += 1
    
    row, column = row + 1, 0


outWorkbook.close()

