import numpy as np
import pandas as pd
import xlrd
from xlrd.formula import _TOKEN_NOT_ALLOWED

def mean_squared_error(y, y_hat, total_samples):
    error = y - y_hat
    error = pow(error, 2) / total_samples
    return error

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def read_dataset(dataset_choice):
    datasets = [r"mnist_dataset.csv", r"./iris_dataset.xlsx"]
    match dataset_choice:
        case 1:
            dataset = pd.read_csv(datasets[0], header = None, delimiter = ",")
            dataset = dataset.to_numpy()
            total_samples, total_features = dataset.shape
            total_features -= 1
            total_classes = 10
        case 2:
            workbook = xlrd.open_workbook(datasets[1])
            dataset = workbook.sheet_by_index(0)
            total_samples = dataset.nrows
            total_features = dataset.ncols - 1
            total_classes = 3
        case _:
            assert("Invalid Dataset Choice")

    return (dataset, total_samples, total_features, total_classes)

def process_dataset(dataset, total_features):
    samples_features = dataset[ :, 0:total_features]
    samples_classes = dataset[ :, total_features:]
    return (samples_features, samples_classes)