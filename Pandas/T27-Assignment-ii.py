#ii)Print all columns
import pandas as pd
df = pd.read_csv('balloons_dataset.csv')
X = df.drop('inflated',axis = 1)
y = df['inflated']
print(df.columns)

'''
===================OUTPUT========================
Index(['color', 'size', 'act', 'age', 'inflated'], dtype='object')
'''