import heapq

arr1 = [1,2,3,4,5,6,7,3,4,6]

# 找出列表中最大的三个元素
a = heapq.nlargest(3, arr1) # [7, 6, 6]
print(a)

# 找出列表中最小的三个元素
b = heapq.nsmallest(3, arr1) # [1, 2, 3]
print(b)

list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

# 找出价格最高的三个股票
c = heapq.nlargest(3, list2, key=lambda x: x['price'])
print(c)

# 找出持有股票最多的两个人
d = heapq.nlargest(2, list2, key=lambda x: x['shares'])
print(d)
