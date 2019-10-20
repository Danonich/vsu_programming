ex = input()
sym = {'+', '-', '*', '/', '//', '**'}
op = ''.join(sym & set(ex))
index = ex.find(op)
x, y = ex[:index], ex[index + 1:]

if y.find(op) != -1:
    op += op
    y = s[index + 2:]

x, y = float(x), float(y)
op = {
    '+': x + y,
    '-': x - y,
    '*': x * y,
    '/': x / y,
    '//': x // y,
    '**': x**y
}
print(op[op])
