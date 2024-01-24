'''
Write a Python Program to Check whether a String “Madam” is
Palindrome or not ?
'''
strg = input("Enter the string:")
strg=strg.lower()
print
revg = reversed(strg)
print(revg)
if list(strg)==list(revg):
    print("String {} is Palindrome".format(strg))
else:
    print("String {} is not Palindrome".format(strg))

