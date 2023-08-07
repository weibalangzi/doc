a = 'today is bad day'

# 1.统计字符串中每个字符出现的次数
# 方法一
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print(b) # {'t': 1, 'o': 1, 'd': 2, 'a': 3, 'y': 2, ' ': 3, 'i': 1, 's': 1, 'b': 1}

# 方法二
c = {}
for i in a:
    c[i] = c.get(i, 0) + 1
print(c) # {'t': 1, 'o': 1, 'd': 2, 'a': 3, 'y': 2, ' ': 3, 'i': 1, 's': 1, 'b': 1}