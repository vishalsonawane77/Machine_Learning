import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('StudentsPerformance.csv')

sns.barplot(x='gender',y='math score',data=df)

plt.show()