def fibbonachi(x):
    a = [0, 1]
    for i in range(x - 2):
        a.append(a[-1] + a[-2])
    print(a)

n = int(input())
fibbonachi(n)
