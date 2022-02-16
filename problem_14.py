num = 1
len_longest_chain = 0
longest_chain = []
result = 0

while num < 1000000:
    n = num
    n_list = []
    while n != 1:
        n_list.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    n_list.append(1)

    if len(n_list) > len_longest_chain:
        len_longest_chain = len(n_list)
        longest_chain = (n_list[:])
        result = num
    num = num + 1

print(result, longest_chain, len_longest_chain)
