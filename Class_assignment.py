class Student: #클래스는 객체지향프로그래밍에서 특정 개체를 생성하기 위해 변수와 메소드를 정의하는 틀이다.
    def __init__(self, name, grade, student_number, sex, address, phone_number, year):
        #__init__은 초기화를 위한 함수이다.
        #self에는 인스턴스 자체가 전달되어있다.
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year
        
    #introduce 메소드를 통해 정보들을 입력받는다.
    def introduce(self):
        print("이름은 %s이다." % self.name)
        print("학년은 %s이다." % self.grade)
        print("학번은 %s이다." % self.student_number)
        print("성별은 %s이다." % self.sex)
        print("주소는 %s이다." % self.address)
        print("전화번호 %s이다." % self.phone_number)

        if (self.year == 1):
            print("멋사 1년차")
            print("우와 아기사자다 !")
        else:
            print("멋사 %s년차" % self.year)
            print("우와 운영진이다 !")
            
while True : #반복문을 이용하여서 정보를 입력받고 print를 이용하여서 출력한다.
    Class_name = input("객체 명을 입력하시오. (단, 영문으로) : ")
    if (Class_name == "종료"):
        break

    name = input("이름을 입력하시오. (단,한글로) : ")
    grade = int(input("학년을 입력하시오. (단,숫자로) : "))
    student_number = int(input("학번을 입력하시오. (단,숫자로) : "))
    sex = input("성별을 입력하시오. (모를 땐 모른다 라고 입력) : ")
    if (sex == "모른다"):
        sex = "None"
    address = input("주소를 입력하시오. (~시까지만) : ")
    phone_number = int(input("전화번호를 입력하시오. (모를 땐 모른다 라고 입력) : "))
    if (phone_number == "모른다"):
        phone_number = "None"
    year = int(input("멋사 몇년차인가요? (단,숫자로) : "))
            
    Class_name = Student(name, grade, student_number, sex, address, phone_number, year) # 입력받은 값으로 인스턴스를 만든다.
    Class_name.introduce() # introduce 메소드로 입력했던 값들을 출력받는다.