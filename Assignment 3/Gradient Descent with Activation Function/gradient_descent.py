def step_function(value):
    if value <= 1.5:
        return 1
    elif 1.5 < value or value <= 2.5:
        return 2
    elif 2.5 < value:
        return 3 

def calculate_y_hat(sample, weights_vector):
    y_hat = weights_vector[0]
    for i in range(0, 4):
        y_hat += sample[i] * weights_vector[i + 1]
    
    y_hat = step_function(y_hat)
    return y_hat

def calculate_y_actual(dataset, row_index):
    column_index = 4
    y_actual = 0

    class_label = dataset.cell_value(row_index, column_index)
    class_label = class_label.replace(u'\xa0', u' ')

    if class_label == "I. setosa":
        y_actual = 1
    elif class_label == "I. versicolor":
        y_actual = 2
    elif class_label == "I. virginica":
        y_actual = 3

    return y_actual

def get_sample_features(dataset, row_index):
    features = []
    column_index = 0

    for _ in range(0, 4):
        feature = dataset.cell_value(row_index, column_index)
        features.append(feature)
        column_index += 1
    
    return features

def squared_error(dataset, training_samples, weights_vector):
    cost = 0
    total_samples = len(training_samples)
    
    for current_row in training_samples:
        current_sample  = []

        current_sample = get_sample_features(dataset, current_row)
        y_hat = calculate_y_hat(current_sample, weights_vector)
        y_actual = calculate_y_actual(dataset, current_row)

        cost += (y_actual - y_hat) ** 2
        current_row += 1

    cost *= 1 / (2 * total_samples)
    return cost

def update_weights(features, old_weights, y_actual, y_hat, learning_rate):
    new_weights = []

    # Update value for w0.
    w = y_actual - y_hat
    w *= learning_rate 
    w += old_weights[0]
    new_weights.append(w)

    # Update values for w1, w2, w3, w4.
    for i in range(1, 5):
        w = y_actual - y_hat
        w *= learning_rate
        w *= features[i-1]
        w += old_weights[i]
        new_weights.append(w)

    return new_weights