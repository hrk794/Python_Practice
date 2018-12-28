a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)


del a[0]
print(a)

del a[2:4]
print(a)


del a[:]
print(a)


b = "Hi this is a variable"
print(b)


del b
# This print statement is supposed to raise an error
print(b)

