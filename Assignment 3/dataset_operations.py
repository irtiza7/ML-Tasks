import xlrd
import random

def read_dataset(path):
    dataset_workbook = xlrd.open_workbook(path)
    dataset = dataset_workbook.sheet_by_index(0)
    return dataset 

def divide_dataset(dataset):
    total_samples = dataset.nrows - 1
    total_columns = dataset.ncols

    random_samples_indexes = list(range(2, total_samples + 2))
    random.shuffle(random_samples_indexes)

    training_samples_indexes = []
    testing_samples_indexes = []

    number_of_training_samples = int(input("Enter Number of Training Samples: "))

    i = 0
    while i < total_samples:
        if i < number_of_training_samples:
            training_samples_indexes.append(random_samples_indexes[i])
        elif i >= number_of_training_samples:
            testing_samples_indexes.append(random_samples_indexes[i])

        i += 1

    return (training_samples_indexes, testing_samples_indexes)