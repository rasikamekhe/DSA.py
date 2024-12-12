#Write a Python program to maintain club members, sort on roll numbers in ascending
#order. Write function “Ternary_Search” to search whether particular student is member
#of club or not. Ternary search is modified binary search that divides array into 3 halves instead of two.

import array as arr
num = arr.array('i',[])
n=int(input("Enter the no. of elements in array: "))
flag =0
for i in range(n):
 elem=int(input("Enter the element: "))
 num.append(elem)
print("The array is: ",num)
key = int(input("Enter the element you want to find: "))
tsnum=sorted(num)
print("The array after sorting is: ",tsnum)
low =0
high=n-1
for i in range(n):
 mid1=low+(high-low)//3
 mid2=high-(high-low)//3
 if key==tsnum or key==tsnum[mid2]:
 print("Element found!!")
 flag=1
 break
 else:
 if key<tsnum[mid1]:
 high=mid1-1
 elif key>tsnum[mid1] and key<tsnum[mid2]:
 low=mid1=1
 high=mid2-1
 elif key>tsnum[mid2]:
 low=mid2+1
if(flag==0):
 print("Element not found!!!")
