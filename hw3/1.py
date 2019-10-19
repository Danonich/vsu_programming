import re
Ex = input('Example: ')
s = ''.join(re.findall(r'[+, - ,*,/,%,**]', Ex))
index = Ex.find(s)
x, y = Ex.split(s)
x, y = float(x), float(y)
op = {
'+': x + y,
'-': x - y,
'/': x / y,
'*': x * y,
'//': x // y,
'**': x ** y}
print(op[s])

