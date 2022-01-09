import numpy as np
import matplotlib.pyplot as plt
import math
from tabulate import tabulate

interval = (1.92,2.08)

def trueGraph():
    space = np.linspace(1.92,2.08,num=8000)
    pOne = (space-2)**9
    plt.plot(space,pOne,".")
    plt.xlabel("x")
    plt.ylabel("p1(x)")
    plt.title("TRUE")
    plt.grid()
    plt.show()

def homerFunc():
    space = np.linspace(1.92,2.08,num=8000)
    p = 1
    a = [-18,144,-672,2016,-4032,5376,-4608,2304,-512]
    temp =[]
    for s in space:
        for i in a:
            p = p*s + i
        temp.append(p)
        p = 1
    plt.plot(space,temp,".")
    plt.xlabel("x")
    plt.ylabel("p2(x)")
    plt.title("Horner")
    plt.grid()
    plt.show()

def test():
    head = [["x_k","f1","f2"]]
    for i in range(13):
        x = 10**(-i)
        temp1 = (1-math.cos(x))/(math.sin(x)**2)
        temp2 = 1/(1+math.cos(x))
        head.append([x,temp1,temp2])
    print(tabulate(head, headers = "firstrow", tablefmt="grid"))


test()
# homerFunc()