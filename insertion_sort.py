# Get numbers from the users separated by spaces and convert it into a list of numbers

A = list(map(int, input().split()))

n = len(A)


# Insertion sort
for i in range(1, n):
        key = A[i]
        j = i -1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        
        
print(A)
