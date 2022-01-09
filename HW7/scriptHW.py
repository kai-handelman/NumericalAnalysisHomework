import numpy as np
import numpy.linalg as ln
from tabulate import tabulate
import matplotlib.pyplot as plt


def makePlot(fun,c,trueData):
    x = np.linspace(-5,5)
    f = fun(x)
    # np.polyval
    # cF = lambda a: np.sum([np.power(a,i) * c[i] for i in range(len(c))])
    cF = np.polyval(np.flip(c),x)
    # print(x)
    plt.title("f_theta VS. interpolating polynomial")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x,f,'r',label="Original Function")
    plt.plot(x,cF,'b',label="Poly Function using Coeffiecients")
    plt.legend(loc="upper left")
    for i in trueData:
        plt.plot(i[0],i[1], 'bo')
    plt.show()

def main(theta):
    print("Running with theta value of: {}".format(theta))
    #Part 1
    f = lambda x : 1/(1+np.exp(-theta*x))
    tData = np.linspace(-5,5,num=7)
    trueTable = [[t,f(t)] for t in tData]
    header = [["x","f(x)"]]
    print("Part 1: Input and Output of Function")
    print(tabulate(header+ trueTable,headers="firstrow",tablefmt='grid') + "\n")


    #Part 2
    a = [[np.power(trueTable[i][0],t) for t in range(len(trueTable))] for i in range(len(trueTable))]
    b = [[t[1]]for t in trueTable]
    c = ln.solve(a,b)
    print("Part 2: Coeffiecients for Polynomial")
    header = [["x^n","C"]]
    print(tabulate(header + [[i,c[i]]for i in range(len(c))],headers="firstrow",tablefmt='grid') + "\n")
    # makePlot(f,c,trueTable)
    #TODO Make Table

    #Part 3
    nX = np.linspace(-5,5,num=101)
    nY = [[f(t)]for t in nX]
    print("The Mean for Part 3: {}".format(np.average(nY)))
    print("The Standard Deviation for Part 3: {}".format(np.std(nY)))

    #Part 4
    err = 0
    nCF = [np.polyval(np.flip(c),i) for i in nX]
    # cF = lambda a: np.polyval(np.flip(c),a)
    for i in range(len(nX)):
        temp = np.abs(nY[i][0] - nCF[i][0])/np.abs(nY[i][0])
        if temp > err:
            err = temp
    print("Maximum Error: {}".format(err))




main(1)
# print("\n\n\n")
#Part 5
main(10)
