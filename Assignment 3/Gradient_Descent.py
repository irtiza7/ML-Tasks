import xlrd 
import random
import numpy as np
import matplotlib.pyplot as plt

def step(value):
    if value <= 1.5:
        return 1
    elif value > 1.5 or value <= 2.5:
        return 2
    elif value > 2.5:
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

    y_hat = step(y_hat)
    return y_hat

def calculate_cost(y, y_hat):
    cost = (y - y_hat)
    cost = cost ** 2
    cost *= (1 / 2)
    return cost

def update_weights(old_weights, features, y, y_hat, learning_rate):
    new_weights = []
    diff = -1 * (y - y_hat)
    w = old_weights[0] - learning_rate * diff
    new_weights.append(w)
    for i in range(4):
        w = old_weights[i + 1] - learning_rate * diff * features[i]
        new_weights.append(w)

    return new_weights

def plot_cost_graph(costs, iterations):
    plt.plot(
        np.array(iterations), 
        np.array(costs), 
        color = 'green', 
        linestyle = 'dashed', 
        linewidth = 1, marker = 'o', 
        markerfacecolor = 'blue', 
        markersize = 2)
    plt.xlim(-100, 10100)
    plt.ylim(0.00008, 0.1)
    plt.xlabel('Iterations')
    plt.ylabel('Cost')
    plt.title('Cost Graph')
    plt.show()

path = "./iris dataset.xlsx"
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)

dataset = sheet
total_samples = dataset.nrows - 1
random_indexes = list(range(1, total_samples + 1))
random.shuffle(random_indexes)

num_of_train_samples = int(input("Training Samples: "))
maximum_iterations = int(input("Maximum Iterations: "))
weights = [-0.3, 0.2, 0, -0.2, 0.3]
learning_rate = float(input("Learning Rate: "))

train_samples_indexes = [random_indexes[i] for i in range(len(random_indexes)) if i < num_of_train_samples]
test_samples_indexes = [random_indexes[i] for i in range(len(random_indexes)) if i >= num_of_train_samples]

index = 0
costs = []
iters = []
for iteration in range(1, maximum_iterations + 1):
    sample_index = train_samples_indexes[index]
    
    features = get_features(dataset, sample_index)
    y = get_y(dataset, sample_index)
    y_hat = y_hat_without_step(features, weights)
    
    if y != y_hat:
        weights = update_weights(weights, features, y, y_hat, learning_rate)

    cost = calculate_cost(y, y_hat)
    if (iteration % 100) == 0 or iteration == 1:
        iters.append(iteration)
        costs.append(cost)

    index += 1
    if index >= len(train_samples_indexes):
        index = 0

print("____________________TRAINING ENDED____________________")
print(f"Final Weights after {maximum_iterations} Iterations")
for w in weights:
    print(w)

print(f"Final Cost after {maximum_iterations} Iterations = {cost}")
plot_cost_graph(costs, iters)

print()
print("____________________TESTING STARTED____________________")
mismatches = 0
for idx in test_samples_indexes:
    features = get_features(dataset, idx)
    y = get_y(dataset, idx)
    y_hat = y_hat_with_step(features, weights)
    if y != y_hat:
        mismatches += 1

print(f"Total Testing Samples = {len(test_samples_indexes)}")
print(f"Total Mismatches = {mismatches}")

accuracy = 100 - (mismatches / len(test_samples_indexes) * 100)
print(f"Testing Accuracy = {accuracy}%")