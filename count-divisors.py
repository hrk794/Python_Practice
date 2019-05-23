"""
This is a solution to the problem given at https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/


You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

Input Format
The first and only line of input contains 3 space separated integers l, r and k.

Output Format
Print the required answer on a single line.



"""


I, r, k = map(int, input().split())

num_of_divisors = 0

for i in range(I, r+1):
    if i%k == 0:
        num_of_divisors += 1

print(num_of_divisors)
