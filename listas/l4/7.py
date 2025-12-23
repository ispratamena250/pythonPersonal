arr = [None] * 10

for i in range(10):
    arr[i] = int(input())

    if i == 0:
        maior = arr[i]
        menor = arr[i]
        posMaior = i
        posMenor = i

    if i > 0 and arr[i] > maior:
        maior = arr[i]
        posMaior = i

    if i > 0 and arr[i] < menor:
        menor = arr[i]
        porMenor = i

print(f"Maior: {maior} em {posMaior} \nMenor: {menor} em {posMenor}")
