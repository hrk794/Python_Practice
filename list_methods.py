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
