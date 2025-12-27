arr = [None] * 5
count = 0

for i in range(5):
    arr[i] = int(input())

for i in range(5):
    print(arr[i], end=" ")
    count += arr[i]

    if i == 0:
        maior = arr[i]
        menor = arr[i]

    if i > 0 and arr[i] > maior:
        maior = arr[i]

    if i > 0 and arr[i] < menor:
        menor = arr[i]

print()

print(f"Maior: {maior}\nMenor: {menor}\nMedia: {count/5}")
