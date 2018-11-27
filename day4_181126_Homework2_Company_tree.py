# 과제2 - 조직도

class Human():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        pass
    pass

class Colleague(Human):
    level="대리"
    def __init__(self, level):
        self.level=level
        pass
    pass
