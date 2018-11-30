def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                                    # 1 positional argument
print()
parrot(voltage=1000)                                            # 1 keyword argument
print()
parrot(voltage=10000, action="VOOOOOOMMMM")                     # 2 keyword arguments
print()
parrot(action='VOOOOOSSSSSSHHHH', voltage=10000000)             # 2 keyword arguments
print()
parrot('a million', 'bereft of life', 'jump')                   # 3 positional parameters
print()
parrot('a thousand', state='pushing up the daisies')            # 1 positional, 1 keyword
print()

# following would be invalid calls:



