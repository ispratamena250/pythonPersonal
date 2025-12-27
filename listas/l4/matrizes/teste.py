import random

m = [[0 for i in range(3)]for i in range(3)]

for i in range(3):
    for j in range(3):
        m[i][j] = random.randint(1, 100)


for i in range(3):
    print()
    for j in range(3):
        print(m[i][j], end=" ")

print()
