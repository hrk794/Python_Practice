# The append method

list = ['one', 'two', 'three']

list.append('four')

print(list)

# append is quivalent to the following operation.

list[len(list):] = ['five']

print(list)


# The extend method: list.extend(iterable)

list.extend(['six', 'seven', 'eight'])      

print(list)

# extend is equivalent to the following operation

list[len(list):] = ['nine', 'ten', 'eleven']

print(list)


# The insert method

list.insert(0, 'zero')

print(list)

# The remove method:    list.remove(x)

# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.remove('zero')

print(list)


# The pop method. Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
# The item position in the method is optional.

list.pop(9)

print(list)

list.pop()

print(list)

# The clear method

# Remove all items from the list. Equivalent to del a[:].

list.clear()

print(list)


# The index method

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

list = ['one', 'two', 'three', 'four', 'five']

print(list)

print(list.index('three'))

print(list.index('three', 1, 3))

print(list)


# The count method  list.count(x)
# Return the number of times x appears in the list.


list.append('three')

print(list)

print(list.count('three'))

print(list.count('two'))


# The sort method list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.sort()

print(list)


# The reverse method

list.reverse()

print(list)

# The copy method

a = list.copy()

#Return a shallow copy of the list. Equivalent to a[:].

print(a)

print(hex(id(list)))
print(hex(id(a)))

# Note that the copy method creates a different object as opposed to a new pointer to the same object.
