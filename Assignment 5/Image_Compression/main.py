import numpy as np
import k_mean_functions as KM

PATH = "./face.jpg"

def  main(pixels, centroids, colors):
    max_iterations = 50
    rows, _ = pixels.shape
    index = np.zeros(rows)

    while(max_iterations > 0):
        for i in range(len(pixels)):
            min_value = 1000
            for j in range(colors):
                x1, x2, y1, y2 = centroids[j, 0], pixels[i, 0], pixels[i, 1], centroids[j, 1]
                
                dist = KM.euclidean_distance(x2, y1, x1, y2)
                if(dist < min_value):
                    min_value = dist
                    index[i] = j  
        
        for i in range(colors):
            sum_x, sum_y = 0, 0
            count = 0
            
            for j in range(len(pixels)):
                if index[j] == i:
                    sum_x += pixels[j, 0]
                    sum_y += pixels[j, 1]
                    count += 1
            
            if count == 0:
                count = 1

            centroids[i, 0] = float(sum_x / count)
            centroids[i, 1] = float(sum_y / count)

        max_iterations -= 1

    return centroids, index

if __name__ == '__main__':

    image = KM.read_image(PATH)
    k = int(input("Enter Number of Colors> "))

    pixels, centroids = KM.initialize_centroids(image, k)
    centroiids, index = main(pixels, centroids, k)
    KM.compress_face_image(centroids, index, image)