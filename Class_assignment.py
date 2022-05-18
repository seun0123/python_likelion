class Student:
    def __init__(self, Class_name, name, grade, student_number, sex, address, phone_number, year):
        self.Class_name = Class_name
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year
    

    def introduce_Class_name(self):
        print("객체 명을 입력하시오. (단, 영문으로) : %s" % self.Class_name)
    
    def introduce_name(self):
        print("이름을 입력하시오. (단, 한글로) : %s" % self.name)

    def introduce_grade(self):
        print("학년을 입력하시오. (단, 숫자로) : %s" % self.grade)

    def introduce_student_number(self):
        print("학번을 입력하시오. (단, 숫자로) : %s" % self.student_number)

    def introduce_sex(self):
        print("성별을 입력하시오. (모를 때는 모른다 라고 입력.) : %s" % self.sex)
        if(self.sex == "모른다"):
            self.sex = None

    def introduce_address(self):
        print("주소를 입력하시오. (~시까지만) : %s" % self.address)

    def introduce_phone_number(self):
        print("전화번호를 입력하시오. (모를 때는 모른다 라고 입력.) : %s" % self.phone_number)
        if(phone_number == "모른다"):
            phone_number = None

    def introduce_year(self):
        print("이름을 입력하시오. (단, 한글로) : %s" % self.year)
        if(self.year == 1):
            print("멋사 1년차\n 우와 아기사자다!")
        else:
            print("멋사 %s년차\n 우와 운영진이다!")

seun = Student("박세은","1", "202214021", "여자", "서울시", "01030345474", "2")

seun.introduce_Class_name()
seun.introduce_name()
seun.introduce_grade()
seun.introduce_student_number()
seun.introduce_sex()
seun.introduce_address()
seun.introduce_phone_number()
seun.introduce_year()
