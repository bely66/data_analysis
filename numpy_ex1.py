# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 04:37:54 2019

@author: USER
"""

import numpy as np 

my_list = [1,2,3,4]
my_lists = [my_list,[1,2,3,5]]
array1 = np.array(my_lists)
np.arange(5,20,2)
arr1 = np.array([[1,2,3],[8,9,10],[2,4,6]])
arr_zero = np.zeros((10,10))

#getting the array length 
x = arr_zero.shape[1]  
for i in range (x):
    arr_zero[i]=i
#array fancy indexing
arr_zero[[0,1,2,3]]  #prints the lines which contains your values

# Array transposition
arr_t1 = np.arange(50).reshape((10,5))
arr_t1.T ; 
#dot product 
np.dot(arr_t1,arr_t1.T)
 # 3d array 
 arr3d = np.arange(50).reshape((5,5,2))
 
 #array universal functions 
 array1 = np.arange(11)
 array2 = np.array([1,2,4,5,1,6,1,1,1,1,1])
 np.sqrt(array1)
 np.exp(array2)
 array2 = array1.copy()
 A = np.random.randn(10)
 B = np.random.randn(10)
 np.add(A,B)
 np.maximum(A,B)
 #array processing
 
 #mathematical operations 
print (arr1*arr1)
print(arr1+arr1)
print (arr1+4)
print (arr1**3)

arr2 = np.arange(0,11)

#slice of the array
arr3 = arr2[5:11]

arr3[:]=99