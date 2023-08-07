
class Person:
    def __init__(self, name, age):
        # 设置私有属性
        self.__name = name
        self.__age = age
        # 设置受保护的属性
        self._gender = 'man'
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name= name

    def say_age(self):
        print(self.__age)
