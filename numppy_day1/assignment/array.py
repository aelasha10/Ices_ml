#A 1D array with values from 10 to 50 with a step of 5 using np.arange()
import numpy as np
array_list =[1,2,3,4,5]
array_1d = np.arange(10, 55, 10)  #(it use to give the start, stop, step)
print("1D array with values from 10 to 50 with a step of 5:")
print(array_1d)      

#A 3x3 identity matrix using np.eye()
identity_matrix = np.eye(2)   #here we have create the 2 by 2 matrix by using np.eye()
print("3x3 identity matrix:")
print(identity_matrix)

# A 4x5 array filled with the value 7 using np.full()
full_array =np.full((4, 5), 7)  # 4 by 5 matrix created using by using np.full()
print("4x5 array filled by 7:")
print(full_array)

# A 2x3 array with random values between 0 and 1 using np.random.rand()
random_array = np.random.rand(2, 3)  #2 by 3 matrix
print("2x3 array with random values between 0 and 1:")
print(random_array)

