# correlation example

import numpy as np


x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 5, 4, 5])

correlation_matrix = np.corrcoef(x, y)
correlation_coefficient = correlation_matrix[0, 1]

print(correlation_coefficient)
