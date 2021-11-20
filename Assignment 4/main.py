import helping_functions as hf

def main():
    dataset_choice = int(input("Dataset to use? [1] for MNIST and [2] for Iris Flower > "))
    dataset, total_samples, total_features, total_classes = hf.read_dataset(dataset_choice)
    samples_features, samples_classes = hf.process_dataset(dataset, total_features)

if __name__ == '__main__':
    main()