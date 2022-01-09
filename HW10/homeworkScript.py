import numpy as np
import matplotlib.pyplot as plt


def fowardDif(func,x,h):
    return (func(x+h)-func(x))/h

def backwardDif(func,x,h):
    return (func(x)-func(x-h))/h

def centralDif(func,x,h):
    return (func(x+h)-func(x-h))/(2*h)

def getError(approx,truth):
    return np.abs(truth-approx)/np.abs(truth)

def partOne(f,dT,h,x):
    # Setup
   

    # Part 1
    # fowardErr = []
    # backErr = []
    centralErr = []
    for i in h:
        # fowardErr.append(getError(fowardDif(f,x,i),dT))
        # backErr.append(getError(backwardDif(f,x,i),dT))
        centralErr.append(getError(centralDif(f,x,i),dT))
    
    # plt.loglog(h, fowardErr, 'ro-')
    # plt.grid()
    # plt.xlabel('h')
    # plt.ylabel("Relative Error")
    # plt.title("Forward Difference Error")
    # plt.show()

    # plt.loglog(h, backErr, 'ro-')
    # plt.xlabel('h')
    # plt.grid()
    # plt.ylabel("Relative Error")
    # plt.title("Backward Difference Error")
    # plt.show()

    plt.loglog(h, centralErr, 'ro-')
    plt.xlabel('h')
    plt.grid()
    plt.ylabel("Relative Error")
    plt.title("Central Difference Error")
    plt.show()

def partTwo(f,x,h,dT):
    approxDerivErr = []
    for i in h:
        approxDerivErr.append(getError(approxDeriv(f,x,i),dT))

    plt.loglog(h, approxDerivErr, 'ro-')
    plt.xlabel('h')
    plt.grid()
    plt.ylabel("Relative Error")
    plt.title("Relative Error for an Approximated Derivative")
    plt.show()


def helper():
    xT = 0.2
    deriFunc = lambda x: np.cos(4.8*np.pi*x)*4.8*np.pi
    deriTruth = deriFunc(xT)
    h = [np.power(2.,-i) for i in range(5,31)]
    h.reverse()
    func = lambda x: np.sin(4.8*np.pi*x)
    arrErr = []
    for i in h:
        # arrErr.append(getError(centralDif(func,xT,i),deriTruth))
        arrErr.append(getError(approxDeriv(func,xT,i),deriTruth))
    temp = np.log(arrErr[16])-np.log(arrErr[len(arrErr)-2])
    temp2 = np.log(h[16])-np.log(h[len(arrErr)-2])
    print(temp/temp2)

def approxDeriv(func,x,h):
    return (2*func(x+h) + 3*func(x) - 6*func(x-h) + func(x-2*h))/(6*h)

def main():
    xT = 0.2
    h = [np.power(2.,-i) for i in range(5,31)]
    h.reverse()
    func = lambda x: np.sin(4.8*np.pi*x)
    deriFunc = lambda x: np.cos(4.8*np.pi*x)*4.8*np.pi
    deriTruth = deriFunc(xT)

    partOne(func,deriTruth,h,xT)
    # partTwo(func,xT,h,deriTruth)
    
helper()
# main()