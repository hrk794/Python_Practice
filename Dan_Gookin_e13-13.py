# This code was written to write a c program in the Exercise 13-13 mentioned in the book 
# Beginning Programming with C for Dummies by Dan Gookin
# I felt the C code mentioned in the book was too much to write,
# so instead, wrote a python program to write the C source.


print("#include <stdio.h>")
print()

print("int main()")
print("{")


print()

nums = list(range(15, 9, -1))

for num in nums:
    print('    printf("%%' + str(num) + 's = %' + str(num) + 's\\n","hello");')
    
    
nums = list(range(9, 3, -1))

for num in nums:
    print('    printf(" %%' + str(num) + 's = %' + str(num) + 's\\n","hello");')
    


print("    return 0;")

print("}")
