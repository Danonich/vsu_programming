from random import randint


def odd_even(data):
    n = len(data)
    is_sorted = 0
    while not is_sorted:
        is_sorted = 1
        for i in range(1, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = 0

        for i in range(0, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_sorted = 0
    return data


rand = [randint(0, 10) for i in range(15)]
print(rand)
data = odd_even(rand)
print(data)
