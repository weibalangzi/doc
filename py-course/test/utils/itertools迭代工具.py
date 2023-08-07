import itertools

a = 'ABCD'

# 全排列
for i in itertools.permutations(a):
    print(i)

# 全排列，指定长度
for i in itertools.permutations(a, 2):
    print(i)

# 组合
for i in itertools.combinations(a, 2):
    print(i)