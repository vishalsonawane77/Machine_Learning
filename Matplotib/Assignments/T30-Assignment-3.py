'''
Plot bar chart of name and precentage
Name: Rudra, Mansvi, Jagruti, Neha, kiran
percentage: 71,60,85,56,90
'''

import matplotlib.pyplot as plt
import numpy as np

Name = ["Rudra", "Mansvi", "Jagruti", "Neha", "kiran"]
percentage = [71,60,85,56,90]

x = Name
y = percentage

plt.title("Bar Chart")
plt.xlabel("Name")
plt.ylabel("Percentage")
plt.bar(x,y,color='blue')
plt.show()