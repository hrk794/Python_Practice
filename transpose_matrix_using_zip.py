# Transpose the matrix using the zip() function (actually unzipping a list of lists)


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(matrix)

print()
print()

transpose = list(zip(*matrix))

print(transpose)
