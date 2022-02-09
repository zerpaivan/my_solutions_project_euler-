# problem 8

file = open("number_problem_8.txt", "r")
number = file.read()
number = number.replace("\n", "")
file.close()
adj_digit = 13

x_max = 0
for d in range(len(number)-(adj_digit-1)):
    n = number[d: d + adj_digit]
    x = 1
    for i in n:
        x = x * int(i)
    if x > x_max:
        x_max = x
        solution = n

print(solution, x_max)
