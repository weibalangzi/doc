
# 字面量创建
a = [1,2,3]

# 构造函数创建
b = list(range(1, 4))
print(b)

# 创建重复元素的列表
c = ['girl'] * 10
print(c)

# 生成式创建列表
d = [i for i in range(1,4)]
print(d)

# 生成式创建列表2
e = [str(i) + j for i in range(1,4) for j in 'abcde']
print(e)