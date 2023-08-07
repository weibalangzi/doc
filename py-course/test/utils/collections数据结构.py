from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

# namedtuple，创建一个自定义的tuple对象
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# deque，双向列表，适用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict，key不存在时返回默认值
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict，按照插入的顺序排列
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

# Counter，计数器
# 创建一个Counter对象
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(fruits)

# 计算元素频率
print(counter)  # 输出: Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(counter['apple'])  # 输出: 3
print(counter['grape'])  # 输出: 0 (不存在的元素返回0)
