

# 把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型
a = 1,2,3
print(a) # (1, 2, 3)

# 把一个元组赋值给多个变量时，元组会解包成多个值
d,e,f = a
print(d) # 1
print(e) # 2
print(f) # 3

# 解包出来的元素个数和变量个数不对应时，会抛出异常
a1 = 1, 10, 100, 1000
 i, j, k = a1             # ValueError: too many values to unpack (expected 3)
 i, j, k, l, m, n = a1    # ValueError: not enough values to unpack (expected 6, got 4)