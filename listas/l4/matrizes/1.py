m = [[0 for _ in range(3)]for _ in range(3)]
count = 0

for i in range(3):
    for j in range(3):
        m[i][j] = int(input())
        if m[i][j] > 10:
            count += 1

print(f"Maiores: {count}")
