
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say_age(self):
        print(self.__age)

class Man(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = 'man'

class Woman(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = 'woman'    


p1 = Man('jack', 18)

p2 = Woman('rose', 17)

p1.say_age()

p2.say_age()