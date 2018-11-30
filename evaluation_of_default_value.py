

def f1(a, L=[]):
    L.append(a)
    return L
# The default value is evaluated once when the function is called for the first time, and the new value is passed to the subsequent calls of the function. 

print(f1(1))
print(f1(2))
print(f1(3))




def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Here we want to preserve the default value of L between multiple calls of f2, each of which return a modified value of L.
# The method used is to keep the default value equal to 'None', and then inside the function check if L is None, and then assign it an empty list. Yet to get to get a clear picture on this

print(f2(1))
print(f2(2))
print(f2(3))

