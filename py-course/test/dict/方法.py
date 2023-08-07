# 字典中的值又是一个字典(嵌套的字典)
students = {
    1001: {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'},
    1002: {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}

# 1.获取1002的信息
a = students.get(1002)
print(a) # {'name': '白元芳', 'sex': True, 'age': 23, 'place': '河北保定'}

# 2.获取1004的信息，如果不存在，返回默认值
b = students.get(1004, {'name': '未知'})
print(b) # {'name': '未知'}

# 获取所有键
c = students.keys()
print(c) # dict_keys([1001, 1002, 1003])
print(list(c)) # [1001, 1002, 1003]

for k1 in c:
    print('k1-->', k1) # 1001, 1002, 1003

# 获取所有值
d = students.values()
print(d) # dict_values({'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}, ...)
print(list(d))

# 获取所有键值对
e = students.items()
print(e) # dict_items([(1001, {'name': '狄仁杰', 'sex': True, 'age': 22, 'place': '山西大同'}), ...])

# 删除1002的信息，并返回被删除的值
f = students.pop(1002)

# 删除1004的信息，如果不存在，返回默认值
g = students.pop(1004, {'name': '未知'})

# 随机删除一个键值对，并以元组的形式返回被删除的键值对
h = students.popitem()

# 设置键值对，如果键不存在，则新增键值对
students.setdefault(1004, {'name': '未知'})

# 更新字典，已存在的键值对会被更新，不存在的键值对会被新增
students.update({1004: {'name': '未知'}})