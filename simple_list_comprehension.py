squares = []

for x in range(10):
    squares.append(x ** 2)

print(squares)


# Same using the lambda tool is as follows:

squares_using_lambda = list(map(lambda x: x**2, range(10)))
print(squares_using_lambda)


# The Simple List Comprehension form is 

squares_using_list_comprehension = [x ** 2 for x in range(10)]
print(squares_using_list_comprehension)



# Other simple examples


# Print the length of each word in the list of names:
names = ['Modi', 'Rahul', 'Gadkari', 'Shah', 'Sonia', 'Jaitley', 'Gehlot', 'Goyal', 'Mayawati', 'Akhilesh', 'Mamta', 'Chandrababu']
length_of_names = [len(name) for name in names]
print(length_of_names)


# Print the last letter of each name in the list of names:

last_letters = [ name[-1] for name in names ]
print(last_letters)

# Print the reverse of each name in the list of names:

reverse_names = [ name[::-1] for name in names ]
print(reverse_names)

# Note that complex expressions can be put in the slot for expression-involving-loop-variable.
#For example, here we build up a list of names, first letters, and
#lengths for each name in the list:

complex_list  = [ [name, name[0], len(name)] for name in names ]
print(complex_list)

