n = 100
sum_x = 0
sum_xsqr = 0
for i in range(1, n + 1):
    sum_x = sum_x + i
    sum_xsqr = sum_xsqr + i ** 2

solution = sum_x ** 2 - sum_xsqr
print(solution)
