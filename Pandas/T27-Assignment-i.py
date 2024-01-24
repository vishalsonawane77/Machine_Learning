'''
1) Read the following dataset balloons_dataset.csv and perform following operations:
i) Print head, tail,
ii)Print all columns
iii)Split data into feature and target variables of given balloons dataset and print feature and target
variable.
'''

#i) Print head, tail,
import pandas as pd
df = pd.read_csv('balloons_dataset.csv')
print(df.head())
print(df.tail())

'''
================OUTPUT=======================
color   size      act       age     inflated
0  YELLOW  SMALL  STRETCH  ADULT        T
1  YELLOW  SMALL  STRETCH  ADULT        T
2  YELLOW  SMALL  STRETCH  ADULT        T
3  YELLOW  SMALL  STRETCH  ADULT        T
4  YELLOW  SMALL  STRETCH  ADULT        T
     color   size  act    age     inflated
95  PURPLE  LARGE  DIP  CHILD        F
96  PURPLE  LARGE  DIP  CHILD        F
97  PURPLE  LARGE  DIP  CHILD        F
98  PURPLE  LARGE  DIP  CHILD        F
99  PURPLE  LARGE  DIP  CHILD        F
'''
