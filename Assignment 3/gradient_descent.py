def step_function(value):
    if value <= 1.5:
        return 1
    elif 1.5 < value or value <= 2.5:
        return 2
    elif 2.5 < value:
        return 3 

def calculate_y_hat(sample, weights_vector):
    y_hat = 0
    for i in range(0, 5):
        y_hat += sample[i] * weights_vector[i]

    return y_hat

# def SE(dataset, weights_vector):
#     row_index, column_index = 1, 0
    
#     cost = 0

#     return cost

# def MSE(weights_vector, y):
#     cost = 0
#     return cost

# def RMSE(weights_vector, y):
#     cost = 0
#     return cost