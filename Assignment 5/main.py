from PIL.Image import MAX_IMAGE_PIXELS
import numpy as np
import matplotlib.pyplot as plt
import cv2
import k_mean_functions as KM

IMAGE_PATH = r'./face.jpg'
MAX_ITERATIONS = 10

image_BGR = cv2.imread(IMAGE_PATH)
image_RGB = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2RGB)
image_height, image_width, _ = image_RGB.shape
# plt.imshow(image)
# plt.show() 

k = int(input("Number of Colors> "))
k_means_list = KM.initialize_random_means(image_RGB, k, image_height, image_width)
book_keeping_array = np.zeros((image_height, image_width))

for _ in range(MAX_ITERATIONS):
    for row_index, image_row in enumerate(image_RGB):
        for pixel_index, pixel in enumerate(image_row):
            
            distances_from_means = []
            for mean in k_means_list:
                distances_from_means.append(KM.euclidean_distance(pixel, mean))
            
            nearest_mean = KM.find_nearest_mean(distances_from_means)
            book_keeping_array[row_index][pixel_index] = nearest_mean
