'''
Ritesh has a salary of 20000 in his company, company givers 10%
hra company also gives 5% ta on salary and deducts 2% tax.
Calculate net salary given to ritesh.
Write a python program to find the net salary of Ritesh.
'''

salary = 20000
hra = 10*20000/100
ta = 5*20000/100
tax = 2*20000/100
final_salary = salary+hra+ta-tax
print(final_salary)


