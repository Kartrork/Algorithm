def number_odd(number):
    odd = []
    for i in range(len(number)):
        if number[i] % 2 == 1:
            odd.append(number[i])
    return odd
print(number_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))