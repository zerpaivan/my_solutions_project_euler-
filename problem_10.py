# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from problem_7 import isPrime
prime_numbers = []
top = 2000000
for i in range(2, top):
    if isPrime(i):
        prime_numbers.append(i)

print(sum(prime_numbers))
