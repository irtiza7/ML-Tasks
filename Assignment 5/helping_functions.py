from PIL.Image import MAX_IMAGE_PIXELS
import numpy as np
import matplotlib.pyplot as plt
import cv2
from random import randint

def distance(point_1, point_2):
    x1, y1, z1 = point_1[0], point_1[1], point_1[2] 
    x2, y2, z2 = point_2[0], point_2[1], point_2[2]
    dist = ((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2)
    return np.sqrt(dist)

def random_means(image, k, image_height, image_width):
    means = []
    for _ in range(k):
        rand_1 = randint(0, image_height - 1)
        rand_2 = randint(0, image_width - 1)
        row = image[rand_1]
        pixel = row[rand_2]
        means.append(pixel)

    return means
        
def select_minimum_distance_mean(distances):
    minimum = min(distances)
    minimum_distance_mean = distances.index(minimum)
    return minimum_distance_mean

def update_book_keeping_array():
    pass