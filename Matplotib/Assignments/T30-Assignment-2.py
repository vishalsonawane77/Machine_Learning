'''
Write a Python programming to create a pie chart with a title popularity of Languages.
languages: hindi, marathi, tamil, telgu, english,gujrathi
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''

import matplotlib.pyplot as plt
import numpy as np

languages = ["hindi", "marathi", "tamil", "telgu", "english","gujrathi"]
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
myexplode = [0.1,0,0,0,0,0]

plt.pie(Popularity,labels = languages,shadow = True,explode = myexplode)
plt.legend(title = "Languages:")
plt.show()


