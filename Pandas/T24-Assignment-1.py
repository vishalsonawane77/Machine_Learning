'''
Perform Sorting along an X axis and y axis.
a = [[23, 42, 16], [12, 43, 26]]
'''

import numpy as np
a = np.array([[23, 42, 16], [12, 43, 26]])
x = np.sort(a,axis=1)       #row wise
print(x)
y = np.sort(a,axis=0)       #column wise
print(y)