file = None

# 读取文件
# 1. read() 读取全部内容
try:
    file = open('test.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('FileNotFoundError')
except LookupError:
    print('LookupError')
except UnicodeDecodeError:
    print('UnicodeDecodeError')
finally:
    if file:
        file.close()