a,b = 'A','a'

c = a + b

d = a + b

# 对比编码大小
print(a > b) # False

print(c == d) # True

# 对比内存地址
print(c is d) # False

