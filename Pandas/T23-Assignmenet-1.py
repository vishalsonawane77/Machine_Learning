'''
Write a python program to compute sum of given np array and
find its mean, median, standard deviation n =
([90,76,48,65,30,54,34,20])
'''
import numpy as np
a = np.array([90,76,48,65,30,54,34,20])

print("Sum given array is:",end="")
print(np.sum(a))

print("Mean of given array is:",end="")
print(a.mean())

print("Median of given array is:",end="")
print(np.median(a))

print("S.D of given array is:",end="")
print(a.std())

'''
===========================OUTPUT=====================================
Sum given array is:417
Mean of given array is:52.125
Median of given array is:51.0
S.D of given array is:22.474638484300478
'''