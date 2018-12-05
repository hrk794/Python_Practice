def f(ham: str, eggs: str = "eggs") -> str:
    print("Annotations: ", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


f('spam')


# Function annotations are completely optional metadata information about the types used by user-defined 
