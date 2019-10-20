x = input()
st = []

while x:
    st.append(x)
    x = input()

for i in set(st):
    print('Element:') 
    print(i) 
    print('repeats:') 
    print(st.count(i))
    print('  ')
