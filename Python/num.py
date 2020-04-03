import numpy as np
a = np.array([1, 2, 3])
a[[0, 0, 0]] = 0
a = np.array([[1, 2, 3], [3, 4, 5]])
b = np.array([[1, 2, 3], [2, 2, 2]])
x = a*b
d = np.array([[1, 2], [2, 3]])
c = a/b
e = a/d
pass
