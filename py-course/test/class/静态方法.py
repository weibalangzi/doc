
class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @staticmethod
    def is_valid_name(name):
        return len(name) >= 3

    @classmethod
    def is_valid_age(cls, age):
        return age >= 18

    @property
    def name(self):
        return self.__name

if Person.is_valid_name('jack'):
    print('jack is a valid name')

# if Person.is_valid_age(17):
#     print('18 is a valid age')

p = Person('jack', 17)

print(p.name)