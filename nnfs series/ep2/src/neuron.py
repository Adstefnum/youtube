import numpy as np

inputs = [0.5, 0.3, 0.2]

weights = [0.2, 0.4, 0.1]
bias = 0.3

output = np.dot(weights, inputs) + bias
print(output)
############################################################

inputs = [0.5, 0.3, 0.2]

weights = [0.2, 0.4, 0.1]
bias = 0.3

output = weights[0]*inputs[0] + weights[1]*inputs[1] + weights[2]*inputs[2]+ bias
print(output)



