import numpy as np
import matplotlib.pyplot as plt
import imageio


def read_image(path):
    face_image = imageio.imread(path)
    face_image = face_image / 255
    return face_image

def initialize_centroids(face_image, colors):
    pixels = np.reshape(
        face_image, (face_image.shape[0] * face_image.shape[1], face_image.shape[2]))
    _, columns = pixels.shape
    centroids = np.zeros((colors, columns))

    for i in range(colors):
        rand_centroid1 = int(np.random.random(1) * 10)
        rand_centroid2 = int(np.random.random(1) * 10)
        centroids[i, 0] = pixels[rand_centroid1, 0]
        centroids[i, 1] = pixels[rand_centroid2, 1]
    return pixels, centroids

def euclidean_distance(x1, y1, x2, y2):
	distance = np.square(x2 - x1) + np.square(y2 - y1)
	distance = np.sqrt(distance)
	return distance

def compress_face_image(centroids, index, image):
    centroid = np.array(centroids)
    compressed = centroid[index.astype(int), :]
    compressed = np.reshape(
        compressed, (
            image.shape[0], 
            image.shape[1], 
            image.shape[2])
    )
    plot_image(compressed)

def plot_image(image):
    plt.imshow(image)
    plt.show()