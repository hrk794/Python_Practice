def concat(*args, sep='/'):
    return sep.join(args)


print(concat("earth", "mars", "venus"))             # sep has its default value, as no value passed to it whwn calling the function.

print()

print(concat("earth", "mars", "venus", sep="."))    # sep is given a value other than its default value.



# *args allows to pass arbitrary number of arguments to be passed when the function is called.
