arr = [None] * 6

for i in range(6):
    arr[i] = int(input())

pos = 5
while(True):
    if pos <= -1: break
    print(arr[pos], end=" ")
    pos -= 1

print()
