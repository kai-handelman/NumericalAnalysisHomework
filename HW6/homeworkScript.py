from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt


def main():
    
    fig = plt.figure(1, figsize =(5,5))
    delta = 0.025
    x1,x2 = np.meshgrid(np.arange(-1.2,1.2,delta), np.arange(-1.2,1.2,delta))

    func1 = x1**3 - x2**3 + x1
    func2 = x1**2 + x2**2 - 1
    plt.contour(x1,x2,func1,[0],colors='r')
    plt.contour(x1,x2,func2,[0],colors='b')
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.grid(True)
    plt.show()

def partTwo():
    derfun1x1 = 3*(x**2)+1
    derfun1x2 = -3*(x**2)
    derfun2x1 = 2*x
    derfun2x2 = 2*x


main()