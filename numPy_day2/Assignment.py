""" Array Slicing Practice
Create a 2D array with the following matrix:

[[10, 20, 30, 40],
 [50, 60, 70, 80],
 [90, 100, 110, 120]] """
import numpy as np
arr =np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(arr)

# to Extract the first two rows
print(arr[0:2])
# to Extract the last two columns
print(arr[:,2:4])

#to extract the mid block values
print(arr[1:3,1:3])
