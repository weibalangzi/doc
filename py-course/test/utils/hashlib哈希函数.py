import hashlib

# md5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# sha256
sha256 = hashlib.sha256()
sha256.update('how to use sha256 in '.encode('utf-8'))
sha256.update('python hashlib?'.encode('utf-8'))
print(sha256.hexdigest())

# sha512
sha512 = hashlib.sha512()
sha512.update('how to use sha512 in '.encode('utf-8'))
sha512.update('python hashlib?'.encode('utf-8'))
print(sha512.hexdigest())