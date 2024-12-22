class Person:
    # pass # pass 는 파이썬에서 아무런 내용이 없다 라는 의미임
    def __init__(self, name_param): # 생성자
        self.name = name_param
        print("hihi i am created", self, self.name)

    def talk(self): # 여기서의 self 는 자기자신을 가져오기 위한 파라미터일 뿐. 인자를 따로 넘겨줄 필요 없다.
        print("안녕하세요 저는", self.name, "입니다")

person1 = Person("유재석")
person1.talk()

person2 = Person("박명수")
person2.talk()