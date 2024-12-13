#Write a Python program to compute following computation on matrix:
#a)Addition of two matrices
#B) Subtraction of two matrices
#c) Multiplication of two matrices
#d) Transpose of a matrix

# Define the addition function for two matrices
def add():
    print("Addition of two matrices is: ")
    for i in range(r1):  # Iterate through rows of the matrices
        for j in range(c1):  # Iterate through columns of the matrices
            ans[i][j] = m1[i][j] + m2[i][j]  # Add corresponding elements from both matrices
    for r in ans:  # Print the resulting matrix row by row
        print(r)

# Define the subtraction function for two matrices
def sub():
    print("Subtraction of two matrices is: ")
    for i in range(r1):  # Iterate through rows of the matrices
        for j in range(c1):  # Iterate through columns of the matrices
            ans[i][j] = m1[i][j] - m2[i][j]  # Subtract corresponding elements of m2 from m1
    for r in ans:  # Print the resulting matrix row by row
        print(r)

# Define the multiplication function for two matrices
def mul():
    print("Multiplication of two matrices is: ")
    for i in range(len(m1)):  # Iterate through rows of the first matrix
        for j in range(len(m2[0])):  # Iterate through columns of the second matrix
            for k in range(len(m2)):  # Iterate through rows of the second matrix
                ans[i][j] += m1[i][k] * m2[k][j]  # Perform matrix multiplication and accumulate the result
    for r in ans:  # Print the resulting matrix row by row
        print(r)

# Define the transpose function for two matrices
def transpose():
    print("Transpose of matrix 1 is: ")
    # Create the transpose of m1 by swapping rows and columns
    ans = [[m1[j][i] for j in range(len(m1))] for i in range(len(m1[0]))]
    for r in ans:  # Print the transposed matrix row by row
        print(r)
    print("Transpose of matrix 2 is: ")
    # Create the transpose of m2 by swapping rows and columns
    ans = [[m2[j][i] for j in range(len(m2))] for i in range(len(m2[0]))]
    for r in ans:  # Print the transposed matrix row by row
        print(r)

# Start the program
op = 1  # Variable to control the loop for repeated operations
r1 = int(input("Enter number of rows for matrix 1: "))     # Input number of rows for the first matrix
c1 = int(input("Enter number of columns for matrix 1: "))  # Input number of columns for the first matrix
r2 = int(input("Enter number of rows for matrix 2: "))     # Input number of rows for the second matrix
c2 = int(input("Enter number of columns for matrix 2: "))  # Input number of columns for the second matrix

# Prompt the user to input data for both matrices
print(".___ENTER DATA FOR MATRICES___")
print("\nEnter data for matrix 1: ")
m1 = [[int(input()) for i in range(c1)] for j in range(r1)]  # Input elements for matrix 1
print("MATRIX 1: ")
for n in m1:  # Print matrix 1 row by row
    print(n)

print("Enter data for matrix 2: ")
m2 = [[int(input()) for i in range(c2)] for j in range(r2)]  # Input elements for matrix 2
print("MATRIX 2: ")
for n in m2:  # Print matrix 2 row by row
    print(n)

# Initialize the result matrix with zero values
ans = [[0 for j in range(c1)] for i in range(r1)]

# Loop to perform operations as long as the user wants
while op == 1:
    print("\n......OPERATIONS.......")
    print("1.Addition")  # Option 1 for addition
    print("2.Subtraction")  # Option 2 for subtraction
    print("3.Multiplication")  # Option 3 for multiplication
    print("4.Transpose")  # Option 4 for transpose
    
    ch=int(input("\nEnter your choice: "))
    
    if ch == 1:  # If user chooses addition
        add()
    elif ch == 2:  # If user chooses subtraction
        sub()
    elif ch == 3:  # If user chooses multiplication
        mul()
    elif ch == 4:  # If user chooses transpose
        transpose()
    else:  # If the choice is invalid
        print("WRONG CHOICE!!!")
    print("Do you want to perform again? Press 1 if yes else press 0: ")
    op = int(input())  # Take input from user to continue or exit the loop
