#Sobre a série (2n+1)/(1-3*sqrt(n))
import matplotlib.pyplot as plt
import math

x = [i for i in range(10000)]
y = [(2*i+1)/(1-3*math.sqrt(i)) for i in x]

plt.plot(x, y)
plt.title("Série (2n+1)/(1-3*sqrt(n))")
plt.xlabel("n")
plt.ylabel("f(n)")
plt.show()
