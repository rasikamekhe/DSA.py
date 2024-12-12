#Write a Python program to store first year percentage of students in array. Write
#function for sorting array of floating point numbers in ascending order using quick sort
#and display top five scores

#Function for accepting the percentage of the Students
def inperc():
    perc = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        perc.append(float(input("Enter the percentage of student {0}: ".format(i + 1))))
    return perc

# Function for performing partition of the Data
def outperc(perc):
    for i in range(len(perc)):
        print(perc[i]) 

# Function for printing the percentage of the Students
def perc_partition(perc, start, end):
    pivot = perc[start]
    lower_bound = start + 1
    upper_bound = end
    while True:
        while lower_bound <= upper_bound and perc[lower_bound] <= pivot:
            lower_bound += 1
        while lower_bound <= upper_bound and perc[upper_bound] >= pivot:
            upper_bound -= 1
        if lower_bound <= upper_bound:
            perc[lower_bound], perc[upper_bound] = perc[upper_bound], perc[lower_bound] #swap lower and upper bound
        else:
            break
    perc[start], perc[upper_bound] = perc[upper_bound], perc[start] #swap pivot and upper bound
    return upper_bound

# Function for performing Quick Sort on the Data
def quicksort(perc, start, end):
    if start < end:
        partition = perc_partition(perc, start, end)  #Find the pivot's correct position and rearrange the list around it.
        quicksort(perc, start, partition - 1)  #Sort the left side of the pivot (elements smaller than the pivot)
        quicksort(perc, partition + 1, end)  #Sort the right side of the pivot (elements larger than the pivot).
    return perc

# Main menu logic
op = 1
unsortedperc = []
sortedperc = []

while op == 1:
    print("\n..........MENU.............")
    print("1. Accept the percentage of students")
    print("2. Display the percentage of students")
    print("3. Perform quick sort on the data")
    print("Enter your choice: ")
    ch = int(input())
    if ch == 1:
        unsortedperc = inperc()
    elif ch == 2:
        print("Student percentages are:")
        outperc(unsortedperc)
    elif ch == 3:
        if unsortedperc:
            print("Percentage of students after performing quick sort:")
            sortedperc = quicksort(unsortedperc, 0, len(unsortedperc) - 1)
            outperc(sortedperc)
        else:
            print("No data to sort! Please enter percentages first.")
    else:
        print("WRONG CHOICE!!!!")

    print("Do you want to perform again? If yes, press 1 else 0: ")
    op = int(input())
