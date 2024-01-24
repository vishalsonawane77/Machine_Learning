'''
Shopkeeper wants to sale his different products by applying
different discounts on the basis of sale price. More sale amount,
more discount. Design good discount scheme for him.
'''

amt = int(input("Enter sale price:"))

def disc():
    print("You get {}% dicount of Rs {} on purchase of {}".format(b,discount,amt))
    print("Your discounted sale price is:",famt)
    print("----Have nice day keep shooping in our shop!!!----")
    
if(amt>0):
    if(2000<=amt<5000):
        b=5                  # b is % of dicount
        discount = b*amt/100
        famt = amt-discount
        disc()
    
    elif(5000<=amt<10000):
        b=10
        discount = b*amt/100
        famt = amt-discount
        disc()
        
    elif(10000<=amt<20000):
        b=15
        discount = b*amt/100
        famt = amt-discount
        disc()
    
    elif(20000<=amt<=30000):
        b=20
        discount = b*amt/100
        famt = amt-discount
        disc()
        
else:
    print("You enter invalid amount")
    