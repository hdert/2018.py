w = input().lower()
l = []
temp = ''
for i in w:
    l.append(i)
for i in range(len(w)):
    temp = l[i]
    l[i] = l[len(w)-i]
    l[len(w)-i] = temp
print(l)
