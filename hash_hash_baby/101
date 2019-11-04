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

set_value('plz', 1)
set_value('plz', 10)

set_value('me', 5)
set_value('me', 25)

set_value('kill', 1)
set_value('kill', 2)

print(storage)

del_value('plz')

print(get_value('plz'))
print(get_value('me'))
print(get_value('kill'))

print(storage)
