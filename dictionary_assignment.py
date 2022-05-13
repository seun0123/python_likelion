Dic1 = {"name":"seun", "age": "20", "birthday" : "0123", "sex" : "female", "phonenum" : "010-3034-5474"}
Dic2 = {"name":"nahyun", "age": "20", "birthday" : "0307", "sex" : "female", "phonenum" : "010-8910-1441"}
Dic3 = {"name":"choenwo", "age": "20", "birthday" : "0417", "sex" : "male", "phonenum" : "010-9339-6369"}

name = [1,2,3]
age = [1,2,3]
birthday = [1,2,3]
sex = [1,2,3]
phonenum =[1,2,3]

name[0] = Dic1["name"]
name[1] = Dic2["name"]
name[2] = Dic3["name"]

age[0] = Dic1["age"]
age[1] = Dic2["age"]
age[2] = Dic3["age"]

birthday[0] = Dic1["birthday"]
birthday[1] = Dic2["birthday"]
birthday[2] = Dic3["birthday"]

sex[0] = Dic1["sex"]
sex[1] = Dic2["sex"]
sex[2] = Dic3["sex"]

phonenum[0] = Dic1["phonenum"]
phonenum[1] = Dic2["phonenum"]
phonenum[2] = Dic3["phonenum"]

print("이름 리스트는 " + str(name))
print("나이 리스트는 " + str(age))
print("생일 리스트는 " + str(birthday))
print("성별 리스트는 " + str(sex))
print("전화번호 리스트는 " + str(phonenum))
