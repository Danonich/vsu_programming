from collections import deque

def is_dota_player(s):
    return not len(s) % 2 and s[0] == 'D'

people = {
    'Alice': ['Bob', 'Diman', 'Vlad', 'Diana'],
    'Vlad': ['Lula', 'Ahmad'],
    'Diana': ['Dima'],
    'Bob': ['Vlad', 'Oleg']
}

deq = deque(people['Alice'])
checked_people = []

while deq:
    chel = deq.popleft()
    if chel not in checked_people:
        if is_dota_player(chel):
            print(chel, 'is play in Dota')
            break
        else:
            deq += people.get(chel, [])
        checked_people.append(chel)
else:
    print('Dont play in Dota')
