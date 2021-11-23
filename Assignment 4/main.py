from math import cos
import numpy as np
import helping_functions as hf

def main():
    # Number of perceptrons in hidden layer.
    PERCEPTRONS = 16

    dataset_choice = int(input("Dataset to use? [1] for MNIST and [2] for Iris Flower > "))
    dataset, total_samples, total_features, total_classes = hf.read_dataset(dataset_choice)
    samples_features_values, samples_classes = hf.process_dataset(dataset, total_features)

    # Randomly iinitializing weights vector and biases vector for level A and B
    weights_vector_A = hf.random_weights_vector(PERCEPTRONS, total_features)
    weights_vector_B = hf.random_weights_vector(total_classes, PERCEPTRONS)
    biases_vector_A = hf.random_biases_vector(PERCEPTRONS, 1)
    biases_vector_B = hf.random_biases_vector(total_classes, 1)

    # Printing dimensions for each level's weights and biases vectors.
    print(f"\nDimensions of Weights Vector for Level A: {(np.array(weights_vector_A)).shape}")
    print(f"Dimensions of Weights Vector for Level B: {(np.array(weights_vector_B)).shape}")
    print(f"Dimensions of Biases Vector for Level A: {(np.array(biases_vector_A)).shape}")
    print(f"Dimensions of Biases Vector for Level B: {(np.array(biases_vector_B)).shape}\n")

    current_sample = 0
    costs = []

    # Feeding each sample to neural network and calculating cost
    for sample_values in samples_features_values:

        # Calculations for Level A
        weighted_sums_A = hf.calculate_weighted_sum(weights_vector_A, sample_values)
        weighted_sums_A = weighted_sums_A.reshape(PERCEPTRONS, 1)
        weighted_sums_A = hf.add_biases(weighted_sums_A, biases_vector_A)
    
        # Applying Sigmoid Activation Function to weighted sums of each perceptron in hidden layer
        hidden_layer_output = []
        for perceptron_output in weighted_sums_A:
            sigmoid = hf.sigmoid(perceptron_output[0])
            hidden_layer_output.append(sigmoid)

        # Converting outputs of hidden layer into 16*1 array
        hidden_layer_output = np.array(hidden_layer_output)
        hidden_layer_output = hidden_layer_output.reshape(PERCEPTRONS, 1)

        # Calculations for Level B
        weighted_sums_B = hf.calculate_weighted_sum(weights_vector_B, hidden_layer_output)
        weighted_sums_B = weighted_sums_B.reshape(total_classes, 1)
        weighted_sums_B = hf.add_biases(weighted_sums_B, biases_vector_B)
    
        # Applying Sigmoid activation function to weighted sums of each perceptron in output layer
        output_layer_results = []
        for perceptron_output in weighted_sums_B:
            sigmoid = hf.sigmoid(perceptron_output[0])
            output_layer_results.append(sigmoid)

        # Converting outputs of output layer into total_classes*1 array
        output_layer_results = np.array(output_layer_results)
    
        # Calculating y_hat by finding the output perceptron with maximum value and adding 1, because array indexes start at 0 
        max_value = np.max(output_layer_results)
        y_hat = list(output_layer_results).index(max_value)
        y_hat += 1

        # Calculating cost of single sample and appending it to array of costs
        y = samples_classes[current_sample]
        costs.append(hf.calculate_cost(y, y_hat))
        current_sample += 1

    final_cost = hf.mean_squared_error(costs, total_samples)
    print(f"Final Cost for All Samples in the Dataset: {final_cost}\n")

if __name__ == 'main':
    main()