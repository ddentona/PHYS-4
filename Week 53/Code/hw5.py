import matplotlib.pyplot as plt
import math
import numpy as np

V0 = 4.5
E = 10
A = 5

def V(x):
    if x > V0:
        return 5
    return 0

def PSI(x):
    isim = (V(x) - E < 0)
    if x > V0:
        psi = A * np.exp((1j if isim else 1) * (math.sqrt(abs(E - V(x))) * x + math.sqrt(abs(E - V(0))) * V0))
    else: 
        psi = A * np.exp((1j if isim else 1) * (math.sqrt(abs(E - V(x))) * x))
    return psi

if __name__ == "__main__":
    print(np.exp(1j * np.pi))

    myV = np.frompyfunc(V, 1, 1)
    myPSI = np.frompyfunc(PSI, 1, 1)

    x = np.arange(0,10,0.1)
    U = myV(x)
    psi = myPSI(x)

    fig, ax = plt.subplots()
    ax.plot(x, U)
    ax.plot(x,psi)

    plt.show()