'''
matrix = []

for i in range(3):
    a = []
    for j in range(3):
        print("Enter a{}{}".format(i+1,j+1),":",end='')
        a.append(int(input()))
    matrix.append(a)
    
    
for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print()


A = []
B = []
sum = []

R1 = int(input("Enter no of rows in A:"))
C1 = int(input("Enter no of coloumn in A:"))
print()
R2 = int(input("Enter no of rows in B:"))
C2 = int(input("Enter no of coloumn in B:"))

if R1==R2 and C1==C2:
    print()
    print("Enter elements of A")
    for i in range(R1):
        a1 = []                           #matrix A loop 
        for j in range(C1):
            print("Enter A{}{}".format(i+1,j+1),":",end='')
            a1.append(int(input()))
        A.append(a1)

    
    print()
    print("Enter elements of B")
    for i in range(R2):
        a2 = []                          #matrix B loop 
        for j in range(C2):
            print("Enter B{}{}".format(i+1,j+1),":",end='') 
            a2.append(int(input()))
        B.append(a2)

    print("Mtrix A:")                   # printing Matrix A
    for i in range(R1):
        for j in range(C1):
            print("",A[i][j],end=" ")
        print() 

    print("Mtrix B:")                   # printing Matrix B
    for i in range(R2):
        for j in range(C2):
            print("",B[i][j],end=" ")
        print()       

    for i in range(R1 or R2):  
        s = []                         #sum loop                      
        for j in range(C1 or C2):
            s.append(A[i][j]+B[i][j] )
        sum.append(s)

    print("Matrix A+B:")                #Printing sum matrix
    for i in range(R1 or R2):
        for j in range(C1 or C2):
            print(sum[i][j],end="  ")
        print()
        
else:
    print("rows and columns of both matrix are not equal")

'''

#for i in range(4):
#    for j in range(4):
#        if(i==j):
#            print(" * ",end='')
#        elif(i!=j):
#            print("  ",end='')
#    print("")  


#for i in range(2):
#    for j in range(4):
#        print("*",end='')      # F pattern
#    print()
#    
#    
#for i in range(2):
#    print("*")
        
#i = 0 
#while(i<4):
#    i=i+1
#    j = 3
#    while(j<4):
#        j = j-1
#        if(i==j):
#              print("*",end='')
#        elif(i!=j):
#              print(" ",end='')
#    print("") 
    
    
for i in range(5):
    for j in range(5):
        if(i==4 and j==4):
              print(" * ",end='')
        if(i==3 and j==3):
              print(" * ",end='')
        if(i==2 and j==2):
              print(" * ",end='')
        if(i==1 and j==1):
              print(" * ",end='')
        else:
              print(" ",end='')
    print("")
    
