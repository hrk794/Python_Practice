def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts ACROSS it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)


# The ** operator is used to unpack the contents of a dictionary while calling the function using the entries as the keyword arguments.
