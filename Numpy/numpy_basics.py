# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:35:24 2018

@author: aniketsha
"""
import numpy as np

my_list = [1,2,3,4,5,6]
print (my_list)

# List to numpy array
arr = np.array(my_list)
print ('\n {} {}'.format(arr, type(arr)))

# 2D numpy array
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(my_mat)
print (mat, type(mat))

#numpy range
my_range = np.arange(0,50,2)
print (my_range, type(my_range))

# 1D zero matrix
my_zeros = np.zeros(20)
print (my_zeros)

#2D zero matrix
my_mat_zeros = np.zeros((2,3))
print (my_mat_zeros)

# 2D one matrix
my_ones = np.ones((3,2))
print (my_ones)

#range of values with equal partition
my_ls = np.linspace(0,5,100)
print (my_ls) 

# identity matrix
id_mat = np.eye(4)
print (id_mat)

# random equal values between 0 and 1
ran_arr = np.random.rand(4)
print (ran_arr)

# get certain random number between range
ran_int = np.random.randint(1, 200, 20)
print (ran_int)

# converting 1D to 2D array
ran_arr = np.arange(0,25)
ran_mat = ran_arr.reshape(5,5)
print (ran_mat)

# min, max, mean of 1D array
ran_arr.max()
ran_arr.min()
ran_arr.mean()

# To return the value of index of the mean, max, min
ran_arr.argmax()
ran_arr.argmin()

# Shape and Reshape of vector
shp_arr = ran_arr.shape
reshp_arr = ran_arr.reshape(5,5)
print (reshp_arr)

# Data type of the variables
ran_arr.dtype
type(ran_arr)
