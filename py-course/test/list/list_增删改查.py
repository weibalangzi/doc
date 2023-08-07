a = [1, 2, 3, 'a']

b = [3, 1, 5]

# 在列表前面追加元素
a.insert(0, 0)
print(a)

# 尾部追加元素
a.append(4)
print(a)

# 删除尾部元素
a.pop()
print(a)

# 指定位置插入元素
a.insert(0, 0)
print(a)

# 删除指定位置的元素
a.pop(0)
print(a)

# 删除指定元素
a.remove('a')
print(a)

# 修改指定位置的元素
a[1] = 'b'
print(a)

# 查找指定元素的位置，如果出现多次，返回第一个位置
print(a.index('b'))

# 查找指定元素的个数
print(a.count('b'))

# 反转列表
a.reverse()
print(a)

# 排序
b.sort()
print(b)

# 复制列表
c = a.copy()
print('复制列表', c)

# 清空列表
a.clear()
print(a)

# 删除列表
del a
# print(a) # NameError: name 'a' is not defined

