
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def sum_multiples(top):

    s = 0
    for i in range(top):

        if i % 3 == 0 or i % 5 == 0:
            s = s + i

    print(s)


if __name__ == "__main__":
    top = 1000
    sum_multiples(top)
