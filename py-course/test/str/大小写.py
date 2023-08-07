# 整个字符串首字母大写
a = 'hello world'
print(a.capitalize()) # Hello world

# 每个单词首字母大写
print(a.title()) # Hello World

# 全部大写
print(a.upper()) # HELLO WORLD

# 全部小写
print(a.lower()) # hello world

# 大小写互换
b = 'AbCd'
print(b.swapcase()) # aBcD

# 字符串居中
print(a.center(20)) # '    hello world     '

# 字符串左对齐
print(a.ljust(20)) # 'hello world         '

# 字符串右对齐
print(a.rjust(20)) # '         hello world'

# 字符串填充
print(a.zfill(20)) # '000000000hello world'