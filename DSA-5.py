#Write a Python program to store first year percentage of students in array. Write
#function for sorting array of floating point numbers in ascending order using
#a) Selection Sort b) Bubble sort and display top five scores.

def Selection_Sort(marks):
 for i in range(len(marks)):
 # Find the minimum element in remaining unsorted array
 min_idx = i
 for j in range(i + 1, len(marks)):
 if marks[min_idx] > marks[j]:
 min_idx = j
 # Swap the minimum element with the first element
 marks[i], marks[min_idx] = marks[min_idx], marks[i]
 print("Marks of students after performing Selection Sort on the list : ")
 for i in range(len(marks)):
 print(marks[i])
  
def Bubble_Sort(marks):
 n = len(marks)
 # Traverse through all array elements
 for i in range(n - 1):
 # Last i elements are already in place
 for j in range(0, n - i - 1):
 # Traverse the array from 0 to n-i-1
 # Swap if the element found is greater than the next element
 if marks[j] > marks[j + 1]:
 marks[j], marks[j + 1] = marks[j + 1], marks[j]
 print("Marks of students after performing Bubble Sort on the list :")
 for i in range(len(marks)):
 print(marks[i])
  
def top_five_marks(marks,k):
 n=len(marks)
 marks.sort(reverse=True)
 # Print the first kth largest elements
 for i in range(k):
 print(marks[i], end=" ")
k = 5
#print(top_five_marks(marks, k))
op =1
marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students (Press ENTER after every students marks): ")
for i in range(0, n):
 ele = int(input())
 marks.append(ele) # adding the element
print("The marks of",n,"students are : ")
print(marks)

while(op==1):
 print("\n.........SELECT THE SORTING YOU WANT TO PERFORM.........")
 print("1. Selection Sort of the marks")
 print("2. Bubble Sort of the marks")
 print("3. Viewing top five marks")
 print("4. Exit")
 ch=int(input("\nEnter your choice: "))
 if (ch==1):
 Selection_Sort(marks)
 if(ch==2):
 Bubble_Sort(marks)
 if(ch==3):
 top_five_marks(marks,k)
 if(ch==4):
 print("\nThanks for using this program!!")
 else:
 print("\nThanks for using this program!!")
 print("Do you want to perform again?\nIf yes, press 1, else print 0")
 op=int(input())
