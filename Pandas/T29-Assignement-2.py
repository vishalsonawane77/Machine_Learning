'''Find the standard deviation, 90 th percentile of given company
data
Sale= [1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5]
'''

import numpy as np
sale  = np.array([1, 5, 8, 9, 7, 11, 8, 12, 14, 9, 5])
SD = np.std(sale)
print("S.D is:",SD)
per = np.percentile(sale,90)
print("percentile is:",per)