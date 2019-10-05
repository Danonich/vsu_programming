def skobki(i):
    opens = i.count('(')
    closes = i.count(')')
    if opens > closes:
        return 'Net ', opens - closes,'zakritoi skobki'
    elif opens < closes:
        return 'Net ', closes - opens,'otkritoi skobki'
    return 'Alo! Skobok net'

print(skobki(input('Example: ')))
