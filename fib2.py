Number = int(input("Find the fibonacci series upto?\n"))

def fib2(n):    # Return fibonacci series up to n 
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    #see below
        a, b = b, a+b
    return result


print(fib2(Number))
