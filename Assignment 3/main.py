import dataset_operations as ds_op
import gradient_descent as gd
import matplotlib.pyplot as py_plot
import numpy as np

DATASET_PATH = "./iris dataset.xlsx"
CLASS_LABELS = {1: "I. setosa", 2: "I. versicolor", 3: "I. virginica"}

dataset = ds_op.read_dataset(DATASET_PATH)
training_samples, testing_samples = ds_op.divide_dataset(dataset)

weights_vector = []
print("Enter Initial Values of Weights")
for i in range(0, 5):
    weight = float(input(f"w{i}: "))
    weights_vector.append(weight)


# label = dataset_sheet.cell_value(1, 4)
# label = label.replace(u'\xa0', u' ')

# row_index, col_index = 1, 4

# x_points = np.array([0, 6])
# y_points = np.array([0, 10])
# pyplot.plot(x_points, y_points)
# pyplot.show()