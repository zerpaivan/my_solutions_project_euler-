file = open("50_digit_numbers_list.txt", 'r')
number_list = file.readlines()
file.close()
sum_i = 0

for number in number_list:
    sum_i = sum_i + int(number.strip())
result = (str(sum_i))[:10]

print(result)
