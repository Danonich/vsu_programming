from random import randint


def odd_even(data):
    n = len(data)
    is_sorted = 0
    while is_sorted:
        is_sorted = 1
        for i in range(1, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = 0
        for i in range(n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = 0
    return data


rand = [randint(0, 100) for i in range(15)]
print(rand)
odd_even(rand)
print(rand)
