# Note: If u are using Python IDLE , please make sure numpy library is
# installed . For checking that : Open Command Prompt -> Type pip install numpy

import numpy as np

array_1D = np.array([1,2,3,4,5,6,7,8,9,10]) # One Dimensional Array -> Vector
print("1D Array\n")
print(array_1D)

array_2D = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # Two Dimensional Array -> Matrix
print("2D Array\n")
print(array_2D)

array_3D = np.array([
    [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]],
    [[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19]],
    [[1,4,7,10,13],[2,5,8,11,14],[3,6,9,12,15]]
                     ]) # Three Dimensional Array -> Tensor
print("3D Array\n")
print(array_3D)

# Accessing Elements Of the Arrays ->

print(array_1D[1]) # Second Element of 1D array

print(array_1D[1] + array_1D[4]) # Sum of Two Elements inside Array

print(array_2D[0,1]) # Element -> Row 1 , Column 2
                              #  OR
                     # Element -> Dimension 0 , Element no. 2

print(array_3D[0,1,2]) # Element -> Matrix 1 : Row 2 , Column 3
                                    # OR
                       # Element -> Dimension 0 : Array 2 -> Element 3

# Sorting Of Arrays

print(np.sort(array_1D))
print(np.sort(array_2D))
print(np.sort(array_3D))

array_new_1D = np.array(["Pune","Mumbai","Chennai","Delhi","Kolkata"])
print(np.sort(array_new_1D)) # Array of strings is also sorted.

# Creation of Special Arrays

from numpy import random

array_random_element = np.random.random(3) # 1D Array of Integers between 0 and 1.
array_random_element_1 = np.random.randint(1,100,5) # 1D Array of Integers

array_of_zeros_1D = np.zeros(3) # 1D array of 0s
array_of_zeros_2D = np.zeros((3,4)) # 2D array of 0s
array_of_zeros_3D = np.zeros(((3,3,3))) # 3D array of 0s

array_of_ones_1D = np.ones(3) # 1D array of 1s
array_of_ones_2D = np.ones((3,4)) # 2D array of 1s
array_of_ones_3D = np.ones(((3,3,3))) # 3D array of 1s

array_of_constant_1D = np.full(3,5) # 1D array of constant integer
array_of_constant_2D = np.full((3,4),7) # 2D array of constant integer
array_of_constant_3D = np.full(((3,3,3)),9) # 3D array of constant integer

diagonal_matrix_array = np.eye(3) # 3 x 3 Diagonal Matrix

print(array_random_element)
print(array_random_element_1)
print("\n1D Array\n")
print(array_of_zeros_1D)
print("\n2D Array\n")
print(array_of_zeros_2D)
print("\n3D Array\n")
print(array_of_zeros_3D)
print("\n1D Array\n")
print(array_of_ones_1D)
print("\n2D Array\n")
print(array_of_ones_2D)
print("\n3D Array\n")
print(array_of_ones_3D)
print("\n1D Array\n")
print(array_of_constant_1D)
print("\n2D Array\n")
print(array_of_constant_2D)
print("\n3D Array\n")
print(array_of_constant_3D)
print("\n3 x 3 Diagonal Matrix\n")
print(diagonal_matrix_array)
