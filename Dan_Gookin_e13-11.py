# This code was written to write a c program in the Exercise 13-12 mentioned in the book 
# Beginning Programming with C for Dummies by Dan Gookin
# I felt the C code mentioned in the book was too much to write,
# so instead, wrote a python program to write the C source.


print("#include <stdio.h>")
print()

print("int main()")
print("{")
print("    float sample1 = 34.5;")
print("    float sample2 = 12.3456789;")

print()
nums = [9.1, 8.1, 7.1, 6.1, 5.1, 4.1, 3.1, 2.1, 1.1]


for num in nums:
    print('    printf("%%' + str(num) + 'f = %' + str(num) + 'f\\n",sample1);')
    

nums = [9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8]

for num in nums:
    print('    printf("%%' + str(num) + 'f = %' + str(num) + 'f\\n",sample2);')

print()

print("    return 0;")

print("}")
