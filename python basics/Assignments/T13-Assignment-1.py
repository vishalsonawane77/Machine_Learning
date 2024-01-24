'''
Write the python program to perform following operation on
dictionary using dict comprehension Creating a new dictionary
with only pairs where the value is larger than d = {'a':11,'b':20,'c':13,'d':14,'e':66}
'''

d = {'a':11,'b':20,'c':13,'d':14,'e':66}
new_dict = {k:v for k,v in d.items() if v>10}
print(new_dict)