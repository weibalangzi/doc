
def add(**kwargs):
    sum = 0
    for i in kwargs:
        sum += kwargs[i]
    return sum

v = add(a=1, b=2, c=3)

print(v)