

def say_hello(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# @say_hello
# def add(x, y):
#     return x + y

# add(1,2)

add = lambda x,y: x + y

say_hello(add)(1,2)
