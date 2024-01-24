#iii)Split data into feature and target variables of given balloons dataset and print feature and target
#variable
import pandas as pd
df = pd.read_csv('balloons_dataset.csv')
X = df.drop('inflated',axis = 1)
y = df['inflated']
print(X.head())
print(y.tail())

'''
================output====================
 color   size      act    age
0  YELLOW  SMALL  STRETCH  ADULT
1  YELLOW  SMALL  STRETCH  ADULT
2  YELLOW  SMALL  STRETCH  ADULT
3  YELLOW  SMALL  STRETCH  ADULT
4  YELLOW  SMALL  STRETCH  ADULT
95    F
96    F
97    F
98    F
99    F
'''