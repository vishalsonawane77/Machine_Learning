'''
Write a python program to test whether none of the elements of
a given array is zero use np.all function.
X=0,11,14,34,56,45
'''
import numpy as np
X=np.array([0,11,14,34,56,45])
print("original array is:")
print(X)
print(np.all(X))   #checks whether all elements in an array are non zero


'''
OUTPUT 
original array is:
[ 0 11 14 34 56 45]
False  "as at zero th index 0 element is present and all elements are not zero"
'''