from PIL.Image import MAX_IMAGE_PIXELS
import numpy as np
import matplotlib.pyplot as plt
import cv2
from random import randint

def euclidean_distance(point_1, point_2):
    dist = 0
    for (coordinate_1, coordinate_2) in zip(point_1, point_2):
        dist += (int(coordinate_1) - int(coordinate_2)) ** 2

    return np.sqrt(dist)

def initialize_random_means(image, k, image_height, image_width):
    means = []
    for _ in range(k):
        rand_1 = randint(0, image_height - 1)
        rand_2 = randint(0, image_width - 1)
        row = image[rand_1]
        pixel = row[rand_2]
        means.append(pixel)

    return means

def find_nearest_mean(distances):
    minimum = min(distances)
    minimum_distance_mean = distances.index(minimum)
    return minimum_distance_mean

def update_means(book_keeping_array, ):
    pass