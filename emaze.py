""" 
This is a solution to the problem given at 
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/



Ankit is in maze. The command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.


For example if he is at (2, 0) and the command is L he will go to (1, 0).

Input:

Input contains a single string.

Output:

Print the final point where he came out.


"""


string = input()

position = [0, 0]

position[0] -= string.count("L")

position[0] += string.count("R")

position[1] += string.count("U")

position[1] -= string.count("D")


print(position[0], position[1], sep=" ")
