a = 'hello world'

# 判断字符串是否以指定字符串开头
print(a.startswith('h')) # True

# 判断字符串是否以指定字符串结尾
print(a.endswith('d')) # True

# 判断字符串是否包含指定字符串
print('llo' in a) # True

# 判断字符串是否不包含指定字符串
print('llo' not in a) # False

# 判断字符串是否只包含数字
print(a.isdigit()) # False

# 判断字符串是否只包含字母
print(a.isalpha()) # False

# 判断字符串是否只包含数字和字母
print(a.isalnum()) # False

# 判断字符串是否只包含空格
print(a.isspace()) # False

# 判断字符串是否只包含小写字母
print(a.islower()) # True

# 判断字符串是否只包含大写字母
print(a.isupper()) # False

# 判断字符串是否只包含标题化的单词
print(a.istitle()) # False

# 判断字符串是否只包含可打印字符
print(a.isprintable()) # True

# 判断字符串是否只包含可显示字符
print(a.isascii()) # True

# 判断字符串是否只包含十六进制字符
print(a.isdecimal()) # False

# 判断字符串是否只包含空格、制表符和换行符
print(a.isidentifier()) # False

# 判断字符串是否只包含小写字母和数字
print(a.islower()) # True

# 判断字符串是否只包含大写字母和数字
print(a.isupper()) # False

# 判断字符串是否只包含小写字母和数字
print(a.isnumeric()) # False