arr = [None] * 10
count = 0

for i in range(10):
    arr[i] = int(input())
    if arr[i] % 2 == 0:
        count += 1

print(f"Pares: {count}")
