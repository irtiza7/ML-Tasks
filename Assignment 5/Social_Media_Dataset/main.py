from PIL.Image import MAX_IMAGE_PIXELS
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import average
from numpy.random.mtrand import poisson
import pandas as pd
import k_mean_functions as KM

drop_columns = [
    "Page total likes",
    "Type",
    "Post Weekday",
    "Post Hour",	
    "Lifetime Post Total Reach",	
    "Lifetime Post Total Impressions",	
    "Lifetime Engaged Users",	
    "Lifetime Post Consumers",	
    "Lifetime Post Consumptions",	
    "Lifetime Post Impressions by people who have liked your Page",	
    "Lifetime Post reach by people who like your Page",	
    "Lifetime People who have liked your Page and engaged with your post"	
]

path = r'./mydataset.csv'
max_itr = 500
k = int(input("Clusters? "))
type_of_error = input("WCSS or BCSS? ").lower()
dataset = pd.read_csv(path, header = 0, delimiter = ",")

# Droping columns from the dataset.
for column in drop_columns:
    dataset.drop(column, axis = 1, inplace = True)

# Replacing '?' with 0 in all the columns of dataset.
dataset = dataset.replace(['?'], 0)

# Converting datatype of columns, with string values, to numeric values.
dataset['like'] = pd.to_numeric(dataset['like'])
dataset['share'] = pd.to_numeric(dataset['share'])
dataset['Paid'] = pd.to_numeric(dataset['Paid'])

dataset = dataset.to_numpy()
total_samples, total_features = dataset.shape

# Randomly choosing samples as means from the dataset.
random_centroids_indexes = np.random.choice(total_samples, k, replace = False)
centroids_list = [dataset[i] for i in random_centroids_indexes]

# A list of lists to store samples against each means; storing clusters.
clusters = [[] for _ in range(k)]

for _ in range(max_itr):
    # Creating and updating clusters.
    clusters = KM.create_clusters(dataset, centroids_list, k)
    
    if type_of_error == "wcss":
        # W.C.S.S. Error for all clusters.
        distances_for_all_clusters = KM.WCSS_Error(dataset, clusters, centroids_list)
        average_WCSS = 0
        for index, dist in enumerate(distances_for_all_clusters):
            # print(f"W.C.S.S. for Cluster {index + 1}: {dist}")
            average_WCSS += dist

        average_WCSS /= k
        print(f"Average W.C.S.S. of all Clusters: {average_WCSS}")

    elif type_of_error == "bcss":
        # B.C.S.S. Error between all clusters.
        distances_between_all_clusters = KM.BCSS_Error(centroids_list)
        average_BCSS = distances_between_all_clusters / k 
        print(f"Average B.C.S.S. between all Clusters: {average_BCSS}")
    
    # Update centroids.
    old_centroids = centroids_list
    centroids_list = KM.update_centroids(dataset, clusters, k, total_features)

    # Checking for convergence.
    if KM.check_convergence(old_centroids, centroids_list, k):
        break

labels = KM.get_clusters_labels(clusters, total_samples)
print(labels)
