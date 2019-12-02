from collections import deque

def potomushto_ti_doter(s):
    return not len(s) % 2 and s[0] == 'D'

people = {
    'Alice': ['Vova', 'Vlados', 'Diana'],
    'Vlados': ['Lila', 'Ahmed'],
    'Diana': ['Daniel'],
    'Vova': ['Vlados', 'Oleja']
}

deq = deque(people['Alice'])
checked_people = []
while deq:
    chel = deq.popleft()
    if chel not in checked_people:
        if potomushto_ti_doter(chel):
            print(chel)
    else:
        deq += people.get(chel, [])
    checked_people.append(chel)
print('Nobody players in Dota')

