'''
Write a python program to Accept number 88 from user and
identify if it is palindrome or not?
'''

num = int(input("Enter the no:"))

rev = 0
temp = num

while temp>0:
    digit = temp%10
    rev = rev*10 + digit 
    temp = temp//10
    
if num == rev:
    print("{} is a palindrome".format(num))
else:
    print("{} is not a palindrome".format(num))