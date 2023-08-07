a = {1, 2, 3, 4}

b = {3, 4, 5, 6}

# 交集
print(a & b) # {3, 4}
print(a.intersection(b)) # {3, 4}

# 并集
print(a | b) # {1, 2, 3, 4, 5, 6}
print(a.union(b)) # {1, 2, 3, 4, 5, 6}

# 差集
print(a - b) # {1, 2}
print(a.difference(b)) # {1, 2}

# 对称差集
print(a ^ b) # {1, 2, 5, 6}
print(a.symmetric_difference(b)) # {1, 2, 5, 6}

# 判断子集
print(a <= b) # False

# 判断超集
print(a >= b) # False

# 判断真子集
print(a < b) # False

# 判断真超集
print(a > b) # False

# 判断不相交，有交集返回False
print(a.isdisjoint(b)) # False

# 判断相交，无交集返回True
print(a.isdisjoint({5, 6, 7})) # True