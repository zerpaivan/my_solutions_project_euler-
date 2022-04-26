

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
from math import pow


def p_sum(base, n):
    num = str(int(pow(base, n)))
    ps = 0
    for i in num:
        ps = ps + int(i)
    return ps


print(p_sum(2, 1000))
