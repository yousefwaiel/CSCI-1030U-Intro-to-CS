list = [0,1,2,3,4,5,6]
nl = []
for i in list:
    if list[i] % 2 == 0:
        nl.append(list[i])

print(sum(nl)/len(nl))