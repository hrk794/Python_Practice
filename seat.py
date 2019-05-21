"""

This is a solution to the problem given at https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/

"""


# Using dictionaries to deduce the front seats and seat type 

facing_seats = {1:11, 2:9, 3:7, 4:5, 5:3, 6:1, 7:-1, 8:-3, 9:-5, 10:-7, 11:-9, 0:-11}

seat_types = {1:'WS', 0:'WS', 2:'MS', 5:'MS', 3:'AS', 4:'AS'}

# Get the number of inputs

T = int(input())


# Getting the N inputs and strring them in an array
N_Array = []


# get the facing seat numbers and seat types
for n in range(0, T):
    N_Array.append(int(input()))
    
for seat in N_Array:
    print(seat + facing_seats[seat%12], end=' ')
    print(seat_types[seat%6])    
