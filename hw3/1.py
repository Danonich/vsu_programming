import re
ex = input('Example: ')
s = ''.join(re.findall(r'[+, - ,*,/,%,**]', ex))
index = ex.find(s)
x, y = ex.split(s)
x, y = float(x), float(y)
op = {
'+': x + y,
'-': x - y,
'/': x / y,
'*': x * y,
'//': x // y,
'**': x ** y}
print(op[s])

