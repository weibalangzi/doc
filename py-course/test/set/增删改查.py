a = {1, 2, 3, 4}

# 新增元素
a.add(5)

# 新增多个元素
a.update({6, 7, 8})

# 删除元素
a.remove(8)

# 删除元素，不存在则不删除
a.discard(9)

# 随机删除元素，并返回删除的元素，集合为空则抛出异常，可用于洗牌
a.pop()

# 清空集合
a.clear()

# 复制集合
b = a.copy()

# 判断元素是否在集合中
print(1 in a) # False

# 判断元素是否不在集合中
print(1 not in a) # True

# 不可修改元素
# 集合中的元素必须是hashable类型，所以集合中不能有列表、字典、集合
# a[0] = 0 # TypeError: 'set' object does not support indexing
