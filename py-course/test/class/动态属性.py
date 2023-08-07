class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('jack', 18)

p.gender = 'boy'

print(p.gender)

# 如上，对象是默认可以动态添加属性的，但是这样的属性是不会被序列化的，也就是说，如果你想要序列化这个对象，那么你就需要在类中定义这个属性，或者使用__slots__属性来限制动态添加属性的范围。





class Person2:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person2('jack', 18)

p2.gender = 'man'

print(p2.gender)

# 如上，使用__slots__属性来限制动态添加属性的范围，这样的话，如果你想要添加一个属性，那么你就必须在__slots__中定义，否则就会报错。