# 字面量创建
a = {a: 1, b: 2}

# 构造函数创建
b = dict(a=1, b=2)

# 通过zip创建
c = dict(zip(['a', 'b'], [1, 2]))
print(c) # {'a': 1, 'b': 2}

# 通过列表创建
d = dict([('a', 1), ('b', 2)])
print(d) # {'a': 1, 'b': 2}

# 通过字典创建
e = dict({'a': 1, 'b': 2})
print(e) # {'a': 1, 'b': 2}

# 通过字典推导式创建
f = {i: i * 2 for i in range(3)}
print(f) # {0: 0, 1: 2, 2: 4}

# 通过fromkeys创建
g = dict.fromkeys(['a', 'b'], 1)
print(g) # {'a': 1, 'b': 1}