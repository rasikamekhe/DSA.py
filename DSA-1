'''Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a)The average score of class
b)Highest score and lowest score of class
c)Count of students who were absent for the test
d)Display mark with highest frequency'''


#ACCEPTING THE INPUT FROM THE USER
import array as arr
count=0 #COUNT IS DECLARED AS GLOBAL VARIABLE
highest=-999 #HIGHEST IS DECLARED AS GLOBAL VARIABLE
def avgscore(array):
    sum=0
    for i in range(0,len(array)):
        if(array[i]!=-1):
            sum=sum+array[i]
    avg=(sum/(n-count)) 
    print("\nAverage score of students: ",avg)

def highlow(array):
    highest=-999
    for i in range(0,len(array)):
        if(array[i]>highest):
            highest=array[i]
    print("\nHighest marks score: ", highest)
    lowest=999
    for i in range(0,len(array)):
        if(array[i]!=-1 and array[i]<lowest):
            lowest=array[i]
    print("\nLowest marks scored: ",lowest)
    
def absent(array):
    count=0
    for i in range(0,len(array)):
        if(array[i]==-1):
            count+=1
    print(count, "students are absent.")
    
def mostmarks():
    mostmarks=max(set(array),key=array.count) 
    #when we pass key to max, we pass a function(here, array.count), as we can't pass function directly
    #to max. count is used to count the real values from array, and set used to delete the duplicate values from our array, eg, {2,3,4,2,2}
    #here 2 is real value and 3,4 are duplicate values
    print("\nMarks with highest frequency: ",mostmarks)
    
op=1
import array as arr 
array=arr.array('i',())
n=int(input("Enter the number of students in class: "))
for i in range(n):
    marks=int(input("\nEnter marks of student and enter -1 if the student is absent: "))
    array.append(marks)
print("\nMraks of students are as follows: ")
for i in range(0,len(array)):
    if(array[i]!=-1):
        print("\nMarks of student[",i,"] is: ", array[i])
    else:
        print("\nStudent [",i,"] is absent!!")
while(op==1):
        print("\n............ENTER OPERATION YOU WANT TO PERFORM.............")
        print("\n1. Count the average score of students")
        print("\n2. Count the highest and lowest marks of student")
        print("\n3. Count the number of students that were absent")
        print("\n4. Display the marks with highest frequency")
        print("\nEnter your choice: ")
        ch=int(input()) 
        if(ch==1):
            avgscore(array)
        elif(ch==2):
            highlow(array) 
        elif(ch==3):
            absent(array)
        elif(ch==4):
            mostmarks()
        else:
            print("\nWRONG CHOICE!!!!")
        print("\nDo you want to perform again? Press 1 if yes else press 0")
        op=int(input())     
