x = input()
st = []

while x:
    st.append(x)
    x = input()

for i in set(st):
    print('Elements:') 
    print(i) 
    print('repeats:') 
    print(st.count(i))
    print('  ')
