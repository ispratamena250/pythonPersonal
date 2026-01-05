import matplotlib.pyplot as plt

p = [i for i in range(1, 20)]
s1 = [1/(i**2 + 30) for i in p]
s2 = [1/i**2 for i in p]

plt.scatter(p, s1, label=r"$1/(n^2 + 30)$")
plt.scatter(p, s2, label=r"$1/n^2$")
plt.title("Teste da comparação para 1/(n^2 + 30) e 1/n^2")
plt.xlabel("n")
plt.ylabel("f(n)")
plt.legend()
plt.show()
