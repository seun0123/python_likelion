from typing import List


Dic_List= {}

while True:
    Dic = {}
    key = int(input("key값 : "))
    value = input("values값 : ")
    Dic[key] = value
    if (key == 0) or (value == "문자열 종료"):
        print("그만")
        print(Dic)
        break

    print(list(Dic.keys()))
    print(list(Dic.values()))
    print(list(Dic.items()))
