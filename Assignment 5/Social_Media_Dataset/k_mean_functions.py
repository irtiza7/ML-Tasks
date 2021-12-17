from PIL.Image import MAX_IMAGE_PIXELS
from matplotlib import colors
import numpy as np

def euclidean_distance(point_1, point_2):
    dist = 0
    for (coordinate_1, coordinate_2) in zip(point_1, point_2):
        dist += (int(coordinate_1) - int(coordinate_2)) ** 2
    return np.sqrt(dist)

def find_nearest_mean(distances):
    minimum = min(distances)
    minimum_distance_mean = distances.index(minimum)
    return minimum_distance_mean

def create_clusters(dataset, means, k):
    clusters = [[] for _ in range(k)]
    for index, sample in enumerate(dataset):
        closest_mean_index = get_closest_mean(sample, means)
        clusters[closest_mean_index].append(index)
    return clusters

def get_closest_mean(sample, means):
    distances = [euclidean_distance(sample, mean) for mean in means]
    closest_mean = find_nearest_mean(distances)
    return closest_mean

def update_centroids(dataset, clusters, k, num_of_features):
    updated_means = np.zeros((k, num_of_features))
    for index, cluster in enumerate(clusters):
        cluster_mean = np.mean(dataset[cluster], axis = 0)
        updated_means[index] = cluster_mean
    return updated_means

def check_convergence(old_means, current_means, k):
    d = []
    for i in range(k):
        d.append(euclidean_distance(old_means[i], current_means[i]))
    dists_sum = np.sum(d)
    return dists_sum == 0

def get_clusters_labels(clusters, num_of_samples):
    labels = np.empty(num_of_samples)

    for index, cluster in enumerate(clusters):
        for sample_index in cluster:
            labels[sample_index] = index
    return labels

def WCSS_Error(dataset, clusters, centroids_list):
    distances_for_all_clusters = []
    
    for cluster, centroid in zip(clusters, centroids_list):
        sum_of_distance = 0
        num_of_points = len(cluster)
        
        for sample in cluster:
            sum_of_distance += euclidean_distance(dataset[sample], centroid)
        
        sum_of_distance /= num_of_points
        distances_for_all_clusters.append(sum_of_distance)
    
    return distances_for_all_clusters

def BCSS_Error(centroids_list):
    bcss = 0
    for i in range(len(centroids_list)):    
        j = i + 1
        while j < len(centroids_list):
            bcss += euclidean_distance(centroids_list[i], centroids_list[j])
            j += 1

    return bcss