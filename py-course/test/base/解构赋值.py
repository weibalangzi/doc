a,b,c = [1,2,3]
print(a) # 1
print(b) # 2
print(c) # 3

a1,b1,c1 = (1,2,3)
print(a1) # 1
print(b1) # 2
print(c1) # 3

a2,b2,c2 = {1,2,3}
print(a2) # 1
print(b2) # 2
print(c2) # 3

a3,b3,c3 = '123'
print(a3) # 1
print(b3) # 2
print(c3) # 3

a4,b4,c4 = {'a':1,'b':2,'c':3}
print(a4) # a
print(b4) # b
print(c4) # c

a5,b5,c5 = {'a':1,'b':2,'c':3}.items()
print(a5) # ('a', 1)
print(b5) # ('b', 2)
print(c5) # ('c', 3)

a6,b6,c6 = {'a':1,'b':2,'c':3}.values()
print(a6) # 1
print(b6) # 2
print(c6) # 3

a7,b7,c7 = {'a':1,'b':2,'c':3}.keys()
print(a7) # a
print(b7) # b
print(c7) # c

# 变量个数少于元素的个数方法，就是使用星号表达式
a8,b8,*c8 = [1,2,3,4]
print(a8) # 1
print(b8) # 2
print(c8) # [3, 4]