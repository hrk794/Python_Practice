number_of_primes = 0
limit = int(input("Upto which number do you want to find prime numbers?\n"))


for n in range(2, limit):
     for x in range(2, n):
             if n%x == 0:
                     print(n, 'equals', x, '*', n//x)
                     break
     else:
             #loop fell through without finding a factor
             print(n, 'is a prime number')
             number_of_primes +=1

print('Total number of prime numbers is ', number_of_primes)

