import numpy as np

input_data = np.array([0.5, 0.3, 0.2])

weights_input_hidden = np.array([[0.2, 0.4, 0.1],
                                 [0.3, 0.2, 0.5],
                                 [0.1, 0.6, 0.3],
                                 [0.4, 0.2, 0.2]])

biases_hidden = np.array([0.3, 0.2, 0.5, 0.1])

hidden_layer_outputs = np.dot(weights_input_hidden, input_data) + biases_hidden
print(hidden_layer_outputs)

#################################################################################################################################################
inputs = [0.5, 0.3, 0.2]

weights1 = [0.2, 0.4, 0.1]
weights2 = [0.3, 0.2, 0.5]
weights3 = [0.1, 0.6, 0.3]
weights4 = [0.4, 0.2, 0.2]

biases = [0.3, 0.2, 0.5, 0.1]

hidden_layer_outputs = [
    weights1[0]*inputs[0] + weights1[1]*inputs[1] + weights1[2]*inputs[2] + biases[0],
    weights2[0]*inputs[0] + weights2[1]*inputs[1] + weights2[2]*inputs[2] + biases[1],
    weights3[0]*inputs[0] + weights3[1]*inputs[1] + weights3[2]*inputs[2] + biases[2],
    weights4[0]*inputs[0] + weights4[1]*inputs[1] + weights4[2]*inputs[2] + biases[3]
]

print(hidden_layer_outputs)
