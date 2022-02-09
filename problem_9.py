# a ** 2 + b ** 2 = c ** 2
# a + b + c = 1000
# a < b < c
# max c value 999 if a = 0 and b = 1
# min c value 335 if a = 332  and b = 333
# max b value 499 if a = 0 and c = 501
for c in range(335, 1000):
    for b in range(1, 500):
        a = 1000 - c - b
        if a ** 2 == c ** 2 - b ** 2:
            print(a, b, c, "product: ", a * b * c)
