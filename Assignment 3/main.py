import xlrd 
import random
import numpy as np

def step(value):
    if value <= 1.5:
        return 1
    elif 1.5 < value or value <= 2.5:
        return 2
    elif 2.5 < value:
        return 3 

def get_features(dataset, index):
    features = [dataset.cell_value(index, col) for col in range(4)]
    return features

def get_y(dataset, index):
    label_index = 4
    label = dataset.cell_value(index, label_index)
    label = label.replace(u'\xa0', u' ')
    
    if label == "I. setosa":
        return 1
    elif label == "I. versicolor":
        return 2
    elif label == "I. virginica":
        return 3

def y_hat_without_step(features, weights):
    y_hat = weights[0]
    for i in range(4):
        y_hat += features[i] * weights[i + 1]

    return y_hat

def y_hat_with_step(features, weights):
    y_hat = weights[0]
    for i in range(4):
        y_hat += features[i] * weights[i + 1]

    return step(y_hat)

def cost(dataset, train_samples_indexes, y, y_hat, weights):
    cost = 0
    for index in train_samples_indexes:
        features = get_features(dataset, index)
        y = get_y(dataset, index)
        y_hat = y_hat_without_step(features, weights)
        cost += (y - y_hat) ** 2
    
    cost *= 1 / (2 * len(train_samples_indexes))
    return cost

def update_weights(old_weights, features, y, y_hat, learning_rate):
    new_weights = []
    w = old_weights[0] + learning_rate * (y - y_hat)
    new_weights.append(w)
    for i in range(4):
        w = old_weights[i + 1] + learning_rate * (y - y_hat) * features[i]
        new_weights.append(w)

    return new_weights

path = "./iris dataset.xlsx"
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

dataset = sheet
total_samples = dataset.nrows - 1
random_indexes = list(range(1, total_samples + 1))
random.shuffle(random_indexes)

train_samples_indexes = []
test_samples_indexes = []

num_of_train_samples = int(input("Training Samples> "))
train_samples_indexes = [index for index in random_indexes if index <= num_of_train_samples]
test_samples_indexes = [index for index in random_indexes if index > num_of_train_samples]

maximum_iterations = int(input("Maximum Iterations> "))
weights = [0.3, 0, -0.1, 0.2, -0.4]