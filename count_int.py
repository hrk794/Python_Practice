"""

This code is a solution to the problem at https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/tutorial/

Count Digits
You are given a string S. Count the number of occurrences of all the digits in the string S.

Input: 
First line contains string S.

Output: 
For each digit starting from 0 to 9, print the count of their occurrences in the string S. So, print  lines, each line containing 2 space separated integers. First integer i and second integer count of occurrence of i. See sample output for clarification.

"""



string = input()

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for letter in string:
    if str.isdigit(letter):
        count[int(letter)] += 1
        
for x in range(10):
    print(x, count[x])
