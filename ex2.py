def positive_numbers(number):
    positive = []
    for i in range(len(number)):
        if number[i] > 0:
            positive.append(number[i])
    return positive
print(positive_numbers([-3, -2, -1, 0, 1, 2, 3] ))