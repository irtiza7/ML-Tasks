from math import cos
import dataset_operations
import gradient_descent as gd
from matplotlib import pyplot as plt

DATASET_PATH = "./iris dataset.xlsx"
CLASS_LABELS = {1: "I. setosa", 2: "I. versicolor", 3: "I. virginica"}

dataset = dataset_operations.read_dataset(DATASET_PATH)
training_samples, testing_samples = dataset_operations.divide_dataset(dataset)

terminate = 0
costs = []
iterations = []
weights_vector = []
max_iterations = int(input("Maximum Iterations? "))
learning_rate = float(input("Learning Rate? "))
print("Enter Initial Values of Weights")

for i in range(0, 5):
    weight = float(input(f"w{i}? "))
    weights_vector.append(weight)

index = 0
temp = 100
for itr in range(0, max_iterations):
    cost = 0
    row_index = training_samples[index]

    sample_features = gd.get_sample_features(dataset, row_index)
    y_actual = gd.calculate_y_actual(dataset, row_index)
    y_hat = gd.calculate_y_hat(sample_features, weights_vector)
    diff = y_actual - y_hat

    if diff != 0:
        cost = gd.squared_error(dataset, training_samples, weights_vector)
        
        if itr == temp:
            costs.append(cost)
            iterations.append(itr)
            print(f"Iteration: {itr}, sample: {row_index}, cost = {cost}")
            temp += 100
        
        weights_vector = gd.update_weights(sample_features, weights_vector, y_actual, y_hat, learning_rate)
    else:
        terminate += 1
        if terminate == len(training_samples):
            break 
    
    index += 1
    if index >= len(training_samples):
        index =  0

print("Training has ended and final weights vector is as follows: ")
print(f"Weights = {weights_vector}")
print(f"Cost = {cost}")

plt.plot(iterations, costs, '-ok')
plt.title("Cost")
plt.ylabel("Cost")
plt.xlabel("Iterations")
plt.show()

# x_points = np.array([0, 6])
# y_points = np.array([0, 10])
# pyplot.plot(x_points, y_points)
# pyplot.show()