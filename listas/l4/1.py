tam = 6
arr = [None] * tam

arr[0] = 1
arr[1] = 0
arr[2] = 5
arr[3] = -2
arr[4] = -5
arr[5] = 7

for i in arr:
    print(i, end=" ")

print()

z = arr[0] + arr[1] + arr[5]
print(f"Soma: {z}")

arr[4] = 100
for i in arr:
    print(i, end=" ")

print()
