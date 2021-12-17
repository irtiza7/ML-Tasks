from PIL.Image import MAX_IMAGE_PIXELS
import numpy as np
import matplotlib.pyplot as plt
import cv2
import k_mean_functions as KM

IMAGE_PATH = r'./face.jpg'
MAX_ITERATIONS = 300

image_BGR = cv2.imread(IMAGE_PATH)
image_RGB = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2RGB)
image_height, image_width, _ = image_RGB.shape
# plt.imshow(image)
# plt.show() 

k = int(input("Number of Colors> "))
k_means_list = KM.initialize_random_means(image_RGB, k, image_height, image_width)
book_keeping_array = np.zeros((image_height, image_width))

for _ in range(MAX_ITERATIONS):
    # Calculating distances and assigning mean to each pixel in book keeping array.
    for row_index, image_row in enumerate(image_RGB):
        for pixel_index, pixel in enumerate(image_row):
            
            distances_from_means = []
            for mean in k_means_list:
                distances_from_means.append(KM.euclidean_distance(pixel, mean))
            
            nearest_mean = KM.find_nearest_mean(distances_from_means)
            book_keeping_array[row_index][pixel_index] = nearest_mean

    # Updating means' values.
    temp_means_list = KM.initialize_temp_means(k)
    print(image_RGB.shape)
    for v in temp_means_list:
        print(v[0])
    # print(len(temp_means_list), len(temp_means_list[0]))
    # for row_index, row in enumerate(book_keeping_array):
    #     for mean_index, mean in enumerate(row):
    #         temp_means_list[int(mean)][0] += image_RGB[row_index][mean_index][0]
    #         temp_means_list[int(mean)][1] += image_RGB[row_index][mean_index][1]
    #         temp_means_list[int(mean)][2] += image_RGB[row_index][mean_index][2]
            
    print(temp_means_list)
    break