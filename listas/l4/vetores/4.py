arr = [None] * 8

for i in range(8):
    arr[i] = int(input())

print("Digite x: ", end=" ")
x = int(input())
print("Digite y: ", end=" ")
y = int(input())

print(f"Soma: {arr[x]+arr[y]}")
