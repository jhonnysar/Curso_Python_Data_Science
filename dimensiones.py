import numpy as np


escalar = np.array(42)
print(type(escalar))
print(escalar)


vector = np.array([30,29,35,31,33,36,42])
print(vector)


matrix =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)


tensor = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print(tensor)


array_arange = np.arange(10)
print(array_arange)


eye_matrix = np.eye(3)
print(eye_matrix)


diag =np.diag([1,2,3])
print(diag)


random = np.random.random((2,3))
print(random)