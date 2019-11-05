storage = [[] for x in range(10)]

def hash(key):
    ind = sum(list(map(ord, key)))
    ind = sum(list(map(int, str(ind))))
    return ind % len(storage)

def set_value(key, value):
    ind = hash(key)
    for i in storage[ind]:
        if key == i[0]:
            i[1] = value
            break    
    else:    
        storage[ind].append([key, value])

def get_value(key):
    ind = hash(key)
    for i in storage[ind]:
        if key == i[0]:
            return i[1]

def del_value(key):
    ind = hash(key)
    for i in storage[ind]:
        if key == i[0]:
            storage[ind].remove(i)
            break

set_value('adc', 1)
set_value('abc', 10)

set_value('cba', 5)
set_value('cba', 25)

set_value('xyz', 1)
set_value('xyz', 2)

print(storage)

del_value('cba')

print(get_value('abc'))
print(get_value('cba'))
print(get_value('xyz'))

print(storage)
