a = ' hello world '

# 去除字符串左边的空格
print(a.lstrip()) # 'hello world '

# 去除字符串右边的空格
print(a.rstrip()) # ' hello world'

# 去除字符串两边的空格
print(a.strip()) # 'hello world'

# 去除字符串左边的指定字符
print(a.lstrip('h')) # 'ello world '

# 去除字符串右边的指定字符
print(a.rstrip('d')) # ' hello worl'

# 去除字符串两边的指定字符
print(a.strip('d')) # ' hello worl'

# 替换指定字符
print(a.replace('l','L')) # ' heLLo worLd '

# 分割字符串
print(a.split(' ')) # ['', 'hello', 'world', '']

# 分割字符串，只分割一次
print(a.split(' ',1)) # ['', 'hello world ']

# 合并字符串
b = ['hello','world']
print('_'.join(b)) # 'hello_world'