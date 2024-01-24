'''
Tina has list of N integers. She wants to partition that list into two sub lists of even and odd
numbers. Write python program which will give solution to Tina.
'''

list = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
        
        
print(even)
print(odd)