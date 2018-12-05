def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)

print(f(0))

print(f(1))

# The above example uses a lambda expression to return a function.

# Another use is to pass a small function as an argument

print()

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

print(pairs.sort(key=lambda pair: pair[1]))

# Yes, I found this code a bit tricky

# Here is an explanation on stackoverflow on how this code works:

# https://stackoverflow.com/questions/29781862/how-does-this-example-of-a-lambda-function-work

#You're using a lambda expression (or anonymous function), to sort your list of tuples based on a certain key. pair[1] indicates that you are sorting with a key of the elements in the index position of 1 in each tuple (the strings). Sorting with strings sorts by alphabetical order, which results in the output you are seeing.

#Were you to use the first element in each tuple as the sorting key for instance (pair[0]), you would then sort in increasing numerical order:



