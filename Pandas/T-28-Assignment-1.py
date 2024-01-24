'''
Perform loc and iloc operations on the given dataframe
a= ([3,6,16,32,18,36,19,38,8,16,5,10])
i) loc[8] ,
ii) df.iloc[:2]
iii) loc[:5] ,
iv) loc[45]
'''

import pandas as pd
a= pd.DataFrame([3,6,16,32,18,36,19,38,8,16,5,10])
print(a)
print(a.loc[8])
print(a.iloc[:2])
print(a.loc[:5])
print(a.loc[45])