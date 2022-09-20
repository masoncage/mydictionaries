from os import remove


text = 'sometxt.txt'
text = open(text, 'r')

list = []
for l in text:
    l = l.split()

    for w in l:
        list.append(w)

list.sort()

Dictionary = {}

for w in list:
    Dictionary[w] = list.count(w)

print('\n{:^8}{:^8}'.format('Word','Count'))

for w in Dictionary:
    print('{:^8}{:^8d}'.format (w,Dictionary[w]))

print("")


        
