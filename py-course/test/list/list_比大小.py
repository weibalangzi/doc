a = [1, 2]

b = [1, 2, 3]

c = [4, 5, 6]

d = [a, b, c, 'hahahah', {'name': 'zhangsan'}]

print(a > b) # False

print(b < c) # True

print(a > c) # False

print(d)

# list中比较大小，连个list长度不相等时，会先比较长度，长度相等时，再比较元素