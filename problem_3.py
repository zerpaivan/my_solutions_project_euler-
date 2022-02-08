# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def prime_factors(num):
    factors = []
    f = 2
    while f <= num:
        if num % f == 0:
            factors.append(f)
            num = num // f
        else:
            f = f + 1
    return factors


def largest_pfactor(factors):
    max_factor = max(factors)
    return max_factor


if __name__ == "__main__":
    num = 600851475143
    factors = prime_factors(num)
    print(largest_pfactor(factors))
