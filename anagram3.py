#Given two strings, a and b , that may or may not be of the same length, 
#determine the minimum number of character deletions required to make a and b anagrams. 
#Any characters can be deleted from either of the strings.

#Input :

#test cases,t
#two strings a and b, for each test case
#Output:

#Desired O/p

#Constraints :

#string lengths<=10000

#Note :

#Anagram of a word is formed by rearranging the letters of the word.

#For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.








import string

# Get the numbers of cases from user


T = int(input())

# Get the test cases from the user and store in an array 

cases1 = []
cases2 = []

for case in range(0, T):
     cases1.append(input())
     cases2.append(input())
     

# This function makes a list of counts of occurence of all alphabets in word given to it.     
def count_list_of_word(word):
    count_array = []
    for char in string.ascii_lowercase:
        count_array.append(word.count(char))
    return count_array


# This adds up all the difference values in the corresponding element of two numeric list.    
def diff_list(list1, list2):
    diff = 0
    for i in range(0, len(list1)):
        diff += (abs(list1[i] - list2[i]))
    return diff
        


for case in range(0, T):
    a = diff_list(count_list_of_word(cases1[case]), count_list_of_word(cases2[case]))
    print(a)
