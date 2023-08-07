
# break会跳出整个循环，不管是while还是for
for i in range(1, 100):
    if i > 3:
        break
    print(i)

j = 0

while True:
    if j > 3:
        break
    j += 1
    print(j)