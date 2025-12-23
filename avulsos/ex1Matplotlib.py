import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [i**4 + 3*i**2 -7 for i in x]

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Pequeno exercício")
plt.show()
