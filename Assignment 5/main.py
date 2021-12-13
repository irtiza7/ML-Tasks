from PIL.Image import MAX_IMAGE_PIXELS
import numpy as np
import matplotlib.pyplot as plt
import cv2
import helping_functions as hf

IMAGE_PATH = r'./face.jpg'
MAX_ITERATIONS = 10

image_BGR = cv2.imread(IMAGE_PATH)
image_RGB = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2RGB)
image_height, image_width, _ = image_RGB.shape
# plt.imshow(image)
# plt.show() 

k = int(input("Number of Colors> "))
k_means_list = hf.random_means(image_RGB, k, image_height, image_width)

book_keeping_array = np.zeros((image_height, image_width))

for _ in range(MAX_ITERATIONS):
    
    for image_row in image_RGB:
        
        for image_pixel in image_row:
            
            distances_from_means = []
            for mean in k_means_list:
                print(mean)
                distances_from_means.append(hf.distance(image_pixel, mean))

            print("\n",distances_from_means)
            break
        break
    break