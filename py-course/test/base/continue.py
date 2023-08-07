
# continue会跳出当前循环，所以不会打印出偶数
for i in range(1, 100):
    if i % 2 == 0:
        continue
    print(i)

j = 1

while j < 100:
    j += 1
    if j % 2 == 0:
        continue
    print(j)