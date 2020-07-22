
var_a = ['a', 'b', 'c', 'd']

# for val in var_a:
#     print(val)
    
# for i in range(len(var_a)):
#     print(i)


# for i in range(10):
#     print(i)

# for i in var_a:
#     if i == 'c':
#         break
#     print(i)

# print('aaaa')

for val in var_a:
    if val == 'c':
        continue
    print(val)

var_b = tuple(var_a)

print(type(var_a))
print(type(var_b))
print(var_b)