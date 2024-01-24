'''
1)plot the simple line chart of following data x = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5] y = [3, 7, 9, 6, 4, 5,
14, 7, 6, 16, 12]
'''

import matplotlib.pyplot as plt

x = [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
y = [3, 7, 9, 6, 4, 5, 14, 7, 6, 16, 12]

font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'green','size':20}

plt.title("Plot 1",fontdict = font2)
plt.xlabel("X-axis",fontdict = font1)
plt.ylabel("Y-axis",fontdict = font1)

plt.plot(x,y,marker="o")
plt.grid()
plt.show()