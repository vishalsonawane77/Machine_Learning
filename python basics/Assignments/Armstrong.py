'''
Write a python program to Accept a Number 370 from user and
find if it is Armstrong or not?n = int(input("Enter the no of digit:"))
'''
n = int(input("Enter the no of digit:"))
num = int(input("Enter the no:"))

sum = 0
temp = num

while temp>0:
    digit = temp%10
    sum = sum + digit**n
    temp = temp//10

if num==sum:
    print("{} is Armstrong no".format(num))
else:
    print("{} is not Armstrong no".format(num))