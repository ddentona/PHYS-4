import matplotlib.pyplot as plt
import math
import numpy as np

V_0 = 15

E = 10
A = 5
n = 0
λ = (2*math.pi) / (math.sqrt(abs(E - V_0)))
L = n * λ

def V(x):
    if x > (n+1) * λ:
        return 0
    elif x > n * λ:
        return V_0
    return 0

def PSI(x):
    isim = (V(x) - E < 0)
    if x > n * λ:
        psi = A * np.exp((1j if isim else 1) * (math.sqrt(abs(E - V(x))) * (x - n * λ)))
    else: 
        psi = A * np.exp((1j if isim else 1) * (math.sqrt(abs(E - V(x))) * x))
    return psi

def PSI2(x):
    if x > L/2:
        return np.exp(x - L/2)
    elif x < -L/2:
        return np.exp(-x - L/2)
    else:
        return 0

if __name__ == "__main__":
    print(np.exp(1j * np.pi))

    myV = np.frompyfunc(V, 1, 1)
    myPSI = np.frompyfunc(PSI, 1, 1)

    x = np.arange(-10,10,0.1)
    U = myV(x)
    psi = myPSI(x)

    fig, ax = plt.subplots()
    ax.plot(x, U)
    ax.plot(x,psi)

    plt.show()