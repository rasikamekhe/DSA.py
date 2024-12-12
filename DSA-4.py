#Write a Python program to maintain club members, sort on roll numbers in ascending
#order. Write function “Ternary_Search” to search whether particular student is member
#of club or not. Ternary search is modified binary search that divides array into 3 halves instead of two.

import array as arr

# Initialize an empty array
num = arr.array('i', [])
n = int(input("Enter the number of elements in the array: "))

# Input elements
for i in range(n):
    elem = int(input("Enter the element: "))
    num.append(elem)

print("The array is:", num)

# Input the key to search for
key = int(input("Enter the element you want to find: "))

# Sort the array
tsnum = sorted(num)
print("The array after sorting is:", tsnum)

# Ternary Search
low = 0
high = n - 1
flag = 0  # To track if the element is found

while low <= high:
    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    # Check if the key is at either mid1 or mid2
    if key == tsnum[mid1]:
        print("Element found at index", mid1, "!!")
        flag = 1
        break
    elif key == tsnum[mid2]:
        print("Element found at index", mid2, "!!")
        flag = 1
        break
    else:
        # Narrow the search range
        if key < tsnum[mid1]:
            high = mid1 - 1  # Search in the first third
        elif key > tsnum[mid1] and key < tsnum[mid2]:
            low = mid1 + 1  # Search in the second third
            high = mid2 - 1
        elif key > tsnum[mid2]:
            low = mid2 + 1  # Search in the third third

# If the element is not found
if flag == 0:
    print("Element not found!!!")
