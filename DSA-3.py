#Write a Python program to compute following computation on matrix:
#a)Addition of two matrices
#B) Subtraction of two matrices
#c) Multiplication of two matrices
#d) Transpose of a matrix#

def add():
    print("Addition of two matrices is: ")
    for i in range(r1):
        for j in range(c1):
            ans[i][j]=m1[i][j]+m2[i][j]
    for r in ans:
        print(r)
        
def sub():
    print("Subtraction of two matrices is: ")
    for i in range(r1):
        for j in range(c1):
            ans[i][j]=m1[i][j]-m2[i][j]
    for r in ans:
        print(r) 
        
def mul():
    print("Multiplication of two matrices is: ")
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                ans[i][j]+=m1[i][k]*m2[k][j]
    for r in ans:
        print(r)
        
def transpose():
    print("Transpose of matrix 1 is: ")  
    ans=[[m1[j][i] for j in range(len(m1))] for i in range(len(m1[0]))]
    for r in ans:
        print(r)
    print("Transpose of matrix 2 is: ")
    ans=[[m2[j][i] for j in range(len(m2))] for i in range(len(m2[0]))]    
    for r in ans:
        print(r)
        
op=1
r1=int(input("Enter number of rows for matrix 1: "))  
c1=int(input("Enter number of columns for matrix 1: "))                                              
r2=int(input("Enter number of rows for matrix 2: "))                                              
c2=int(input("Enter number of columns for matrix 2: "))  
print(".............ENTER DATA FOR MATRICES...........")
print("\nEnter data for matrix 1: ")
m1=[[int(input())for i in range(c1)] for j in range(r1)]
print("MATRIX 1: ")
for n in m1:
    print(n)
print("Enter data for matrix 2: ")
m2=[[int(input())for i in range(c2)] for j in range(r2)]
print("MATRIX 2: ")
for n in m2:
    print(n)
ans=[[0 for j in range(c1)] for i in range(r1)]
while(op==1):
    print("......OPERATIONS.......")
    print("\n1.Addition")
    print("\n2.Subtraction")
    print("\n3.Multiplication")
    print("\n4.Transpose")
    print("Enter your choice: ")
    ch=int(input())
    if(ch==1):
        add()
    elif(ch==2):
        sub()
    elif(ch==3):
        mul()
    elif(ch==4):
        transpose()
    else:
        print("WRONG CHOICE!!!")
    print("Do you want to perfomr again? Press 1 if yes else press 0: ")
    op=int(input())   
    
