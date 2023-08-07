
# 序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，
# 而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。
# 与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization）

import json

# 序列化
# json.dumps()方法返回一个str，内容就是标准的JSON。
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

# json.dump()方法可以直接把JSON写入一个file-like Object。
# json.dump(d, file-like Object)

# 反序列化
# json.loads()方法把JSON的字符串反序列化。
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

# json.load()方法从file-like Object中读取字符串并反序列化。
# json.load(file-like Object)