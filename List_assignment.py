List = []

for i in range(0, 15):
    List.append(i)
    print(List)

for i in List:
    if i % 2 == 0:
        List.remove(i)

print(List)

for i in List:
    if i % 3 == 0:
        List.remove(i)

print(List)

print(List.pop(0))

List.insert(0,2)
List.insert(0,3)
List.sort()

print(List)


    