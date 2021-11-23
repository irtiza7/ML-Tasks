from math import cos
import numpy as np
import pandas as pd
import random

def mean_squared_error(costs, total_samples):
    costs = np.array(costs)
    sum_of_costs = np.sum(costs)
    error = sum_of_costs / total_samples
    return error

def calculate_cost(y, y_hat):
    return (y - y_hat) ** 2

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def read_dataset(dataset_choice):
    datasets = [r"mnist_dataset.csv", r"./modified_iris_dataset.csv"]
    match dataset_choice:
        case 1:
            dataset = pd.read_csv(datasets[0], header = None, delimiter = ",")
            dataset = dataset.to_numpy()
            total_samples, total_features = dataset.shape
            total_features -= 1
            total_classes = 10
        case 2:
            dataset = pd.read_csv(datasets[1], header = None, delimiter = ",")
            dataset = dataset.to_numpy()
            total_samples, total_features = dataset.shape
            total_features -= 1
            total_classes = 3
        case _:
            assert("Invalid Dataset Choice")

    return (dataset, total_samples, total_features, total_classes)

def process_dataset(dataset, total_features):
    samples_features = dataset[:, 0 : total_features]
    samples_classes = dataset[:, total_features :]
    return (samples_features, samples_classes)

def random_weights_vector(rows, cols):
    random_weights = []
    for _ in range(rows):
        temp = []
        for _ in range(cols):
            temp.append(round(random.uniform(-0.5, 0.5), 1))
        
        random_weights.append(temp)

    return random_weights

def random_biases_vector(rows, cols):
    random_biases = []
    for _ in range(rows):
        temp = []
        for _ in range(cols):
            temp.append(round(random.uniform(-0.5, 0.5), 1))
        
        random_biases.append(temp)

    return random_biases

def calculate_weighted_sum(weights_vector, input_vector):
    weighted_sum = np.dot(weights_vector, input_vector)
    return weighted_sum

def add_biases(weighted_sum, biases_vector):
    return np.add(weighted_sum, biases_vector)