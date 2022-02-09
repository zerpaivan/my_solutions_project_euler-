# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10 001st prime number?


def isPrime(num):
    is_prime = True
    if num == 2:
        return is_prime

    for factor in range(2, 1 + num // 2):
        if num % factor == 0:
            is_prime = False
            break
    return is_prime


def x_prime_num(place):
    prime_count = 0
    num = 2
    while prime_count < place:
        if isPrime(num):
            prime_count = prime_count + 1

        num = num + 1

    return num - 1


if __name__ == "__main__":
    print(x_prime_num(10001))
