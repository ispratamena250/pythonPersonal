arr = [None] * 10
ans = [None] * 10

for i in range(10):
    arr[i] = float(input())

for i in range(10):
    ans[i] = arr[i] * arr[i]

for i in range(10):
    print(ans[i], end=" ")

print()
