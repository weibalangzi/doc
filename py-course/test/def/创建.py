
def add(a, b):
    # 判断入参是否数字
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('参数类型错误')
    return a + b

# c1 = add(1,2)
# print(c1) # 3

# c2 = add('a', 'b')
# print(c2) # TypeError: 参数类型错误

## 动态参数
def addDynamic(*args):
    # 判断入参是否数字
    for i in args:
        if not isinstance(i, (int, float)):
            raise TypeError('参数类型错误')
    sum = 0
    for i in args:
        sum += i
    return sum