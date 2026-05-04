import math
import matplotlib.pyplot as plt
import numpy as np

slope = 0.5

def LINE(x, b):
    return slope * x + b

def RECIPROCAL(x, b):
    return x / slope + b

def LIGHT_LINE(x, b):
    return x + b

def LIGHT_BACK(x, b):
    return -x + b

def findIntercept(x, y, m):
    return y - m*x

def findCollision(m1, b1, m2, b2):
    x = (b1 - b2) / (m2 - m1)
    y = m2 * x + b2
    return (x,y)

if __name__ == "__main__":
    myLINE = np.frompyfunc(LINE, 2, 1)
    myRECIPROCAL = np.frompyfunc(RECIPROCAL, 2, 1)
    myLIGHTLINE = np.frompyfunc(LIGHT_LINE, 2, 1)
    myLIGHTBACK = np.frompyfunc(LIGHT_BACK, 2, 1)

    Delta_x = np.arange(0, 100, 1)
    l = myLINE(Delta_x, 0)
    r = myRECIPROCAL(Delta_x, 0)

    l1 = myLINE(Delta_x, findIntercept(30, 40, slope))
    l2 = myLINE(Delta_x, findIntercept(80, 60, slope))

    fig1, ax1 = plt.subplots()
    ax1.plot(Delta_x, l)
    ax1.plot(Delta_x, r)
    ax1.plot(Delta_x, l1, "-.")
    ax1.plot(Delta_x, l2, "-.")

    ax1.plot(30, 40, 'bx', label="A")
    ax1.annotate("A", (30,40))
    ax1.plot(80, 60, 'bx', label="B")
    ax1.annotate("B", (80,60))

    fig1.set_size_inches(5,5)

    ax1.set_xlim(0, 100)
    ax1.set_ylim(0, 100)

    fig2, ax2 = plt.subplots()
    Delta_x2 = np.arange(0, 10, 0.1)
    slope = 10/6
    am_line_1 = myLINE(Delta_x2, 0)
    slope = -1 * slope
    am_line_2 = myLINE(Delta_x2, 20)

    ax2.plot(Delta_x2, am_line_1)
    ax2.plot(Delta_x2, am_line_2)

    ax2.set_xlim(0,6)
    ax2.set_ylim(0,20)

    bdays = [myLIGHTBACK(Delta_x2, 16*(x+1)/8) for x in range(8)] + [myLIGHTBACK(Delta_x2, 16 + 4*(x+1)/8) for x in range(8)]
    bdays_limits = [Delta_x2 <= findCollision(-1, 16*(x+1)/8, 10/6, 0)[0] for x in range(8)] + [Delta_x2 <= findCollision(-1, 16 + 4*(x+1)/8, -10/6, 20)[0] for x in range(8)]
    
    for i in range(len(bdays)):
        ax2.plot(Delta_x2[bdays_limits[i]], bdays[i][bdays_limits[i]], "-.")

    plt.show()