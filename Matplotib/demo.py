import matplotlib.pyplot as plt
import numpy as np
plt.xticks(np.arange(0,51,5))
plt.yticks(np.arange(0,11,1))
plt.title("First Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot([1,2,3,4],[1,4,9,16])
