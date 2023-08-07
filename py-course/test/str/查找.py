a = 'hellow world'

# 查找字符串
# find()方法，返回字符串中第一次出现的位置，如果没有匹配项则返回-1
print(a.find('l')) # 2

# index()方法，返回字符串中第一次出现的位置，如果没有匹配项则抛出异常
print(a.index('l')) # 2

# rfind()方法，返回字符串中最后一次出现的位置，如果没有匹配项则返回-1
print(a.rfind('l')) # 9

# rindex()方法，返回字符串中最后一次出现的位置，如果没有匹配项则抛出异常
print(a.rindex('l')) # 9

# count()方法，返回字符串中匹配项的数量
print(a.count('l')) # 3