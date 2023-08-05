import numpy as np

# list
# x = np.array([2, 3, 4, 4, 4])
# print(x)

# tuple
# x = np.array([2, 3, 4, 4, 4])
# print(x)

####################################
# multi dimensional arrays
#################################

# 2D
# x = np.array([[2, 3, 4, 5], [2, 4, 5, 6]])
# print(x)

# 3D
# x = np.array([[[1, 3], [1, 4]], [[3, 4], [45, 5]]])
# print(x)

#  pre declare the dimension
# x = np.array([1, 2, 3, 4], ndmin=4)
# print(x)
# print(x.ndim)

######################################
#  print dimension value
#################################

# tuple
# t = np.array([2, 3, 4, 4, 4])
# print(t.ndim)

# 1D array
# x = np.array([2, 3, 4, 4, 4])
# print(x.ndim)

# 2D array
# y = np.array([[2, 3, 4, 5], [2, 4, 5, 6]])
# print(y.ndim)

# 3D array
# z = np.array([[[1, 3], [1, 4]], [[3, 4], [45, 5]]])
# print(z.ndim)

###################################
# call by index
##################################

# positive indexing
# z = np.array([[[1, 3], [1, 4]], [[3, 4], [45, 5]]])
# print(z)
# print(z[1][0][0])
# print(z[1, 0, 0])

# negative indexing
# x = np.array([2, 3, 4, 4, 4])
# print(x)
# print(x[-1])
# y = np.array([[2, 3, 4, 5], [2, 4, 5, 6]])
# print(y)
# print(y[1, -1])

###################################
#  array slicing
###################################

# x = np.array([1, 3, 3, 4, 4, 5])
# print(x)
# x[start: end: step]
# print(x[1: 4: 2])

#################################
# dtype - Data Type
#################################

# x = np.array([1.2, 2, 3, 4, 5])
# print(x)
# print(x.dtype)

# ___character codes___ #

# integer - 'i'
# boolean - 'b'
# float - 'f'
# complex - 'c'
# unicode - 'U'
# time - 'm'
# Date Time - 'M'
# object - 'O'

# how to add
# x = np.array([array values], dtype='data type character code ')
# x = np.array([1,2,3,4], dtype='i')
# print(x)
# print(x.dtype)

# convert the data type
# y = x.astype('f')

##################################
# copy vs View numpy array
#################################
# x = np.array([1, 2, 3, 4])
# y = x.copy()
# z = x.view()
# print(x)
# print(y)
# print(z)
#
# x[0] = 9
# print('x - ', x)
# print('y - ', y)
# print('z - ', z)
# print( x.base)
# print(y.base)
# print(z.base)

#############################
# iteration through the array
############################

arr = np.array([[1, 32, 332, 423], [12, 4, 42, 42]])

# #first loop
# for i in arr:
#     print(i)
#
# # second loop
# for i in arr:
#     for j in i:
#         print(j)

# # in simple build in functions numpy array
# for i in np.nditer(arr):
#     print(i)

# chosen pattern
# for i in np.nditer(arr[:, ::2]):  # (start : end : step)
#     print(i)

# element + index
# for i in np.ndenumerate(arr):
#     print(i)'
