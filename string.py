#'''Write a Python program to compute following operations on String:
#a)To display word with the longest length
#b)To determines the frequency of occurrence of particular character in the string
#c)To check whether given string is palindrome or not
#d)To display index of first appearance of the substring
#e)To count the occurrences of each word in a given string'''

def longestlen():
    my_string = input("Enter your sentence: ")
    print(my_string)
    longest=max(my_string.split(), key=len)  #split function is used to seperate the words in string
    print("Word with longest length is: ",longest)
    print("Length of longest word is: ", len(longest))
    
def freqoccurance():
    my_string=input("Enter your string: ")
    print(my_string) 
    #METHOD 1:
    allfreq= {}
    for i in my_string:
        if i in allfreq:
            allfreq[i]+=1
        else:
            allfreq[i]=1 
    print(str(allfreq))
    
    #METHOD 2:
    #c=input("Enter your character: ")
    #for i in my_string:
        #if(c==my_string[i]):
            #c[i]+=1
        #else:
            #c[i]=1
    #print(str)
    
def palindrome():
    my_string=input("Enter your string: ")
    print(my_string)
    rev_string=my_string[::-1]
    if my_string==rev_string:
        print("Your string is PLAINDROME!!")
    else:
        print("Your string is NOT PLAINDROME!!!!")
        
def wordcount():
    my_string=input("Enter your string: ")
    print(my_string)
    occur={}
    sen=my_string.split()
    for i in sen:
        if i in occur:
            occur[i]+=1
        else:
            occur[i]=1
    print("Occurance of each word in a string: ", str(occur))
    
def index():
    my_string=input("Enter your string: ")
    print(my_string)
    substr=input("Enter your word: ")
    if(my_string.find(substr)==-1):
        print("SUBSTRING NOT!!!!")
    else:
        print("SUBSTRING FOUND!!")
        print("Substring found at index: ",my_string.find(substr))
        
op=1
while(op==1):
    print(".......Operations...........")
    print("\n1.Longest length")
    print("\n2.Frequency of occurance")
    print("\n3.Palindrome")
    print("\n4.To find occurance of each word")
    print("\n5.To find index of a word")
    print("\nEnter yout choice: ")
    ch=int(input())
    if(ch==1):
        longestlen() 
    elif(ch==2):
        freqoccurance()
    elif(ch==3):
        palindrome() 
    elif(ch==4):
        wordcount()
    elif(ch==5):
        index()
    else:
        print("WRONG CHOICE!!!")
    print("Do you want to perform again? Press 1 for yes else press 0: ")
    op=int(input())                                                                  
                               
   
