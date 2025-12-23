arr = [None] * 10

for i in range(10):
    arr[i] = int(input())
    if i == 0:
        maior = arr[i]
        menor = arr[i]

    if i > 0 and arr[i] > maior:
        maior = arr[i]

    if i > 0 and arr[i] < menor:
        menor = arr[i]

print(f"Maior: {maior} \nMenor: {menor}")
