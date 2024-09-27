import numpy as np
from scipy.signal import convolve

# exploring convolution

mat_A = np.random.randint(low=1, high=10, size=(5,5))
print("Mat_A = \n", mat_A)

kernel_matrix = np.random.randint(low=0, high=5, size=(3,3))
print("Kernel/Filter = \n", kernel_matrix)

conv_res_mat = convolve(mat_A, kernel_matrix, mode="same")
print("Resultant Convolutional Matrix : \n",conv_res_mat)

print("Shape of Matrix A : ", mat_A.shape)
print("Shape of kernel matrix : ", kernel_matrix.shape)
print("Shape of resultant matrix : ", conv_res_mat.shape)