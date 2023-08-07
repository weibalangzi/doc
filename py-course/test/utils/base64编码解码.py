import base64

content = 'Hello World! this is a test string.'

# 编码
b64_bytes = base64.b64encode(content.encode('utf-8'))
print(b64_bytes)

# 解码
b64_str = base64.b64decode(b64_bytes).decode('utf-8')
print(b64_str)