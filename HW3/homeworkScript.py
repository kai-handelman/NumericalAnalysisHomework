import math
import numpy as np
import matplotlib.pyplot as plt

def newtonMethod(func, derFunc, tol, guess,root):
    cur = guess
    if derFunc(root) == 0:
        return None
    else:
        cur = guess
        while abs(cur - root) > tol:
            try:                                        #Check if the derivate function at x_n is 0
                cur = cur - (func(cur)/derFunc(cur))
            except:
                return None
    if cur != cur:                                        #Check cur ends up at nan
        return None
    return cur

def hwHelper(showVisuals):
    func = lambda x: 1/(np.exp(x)+1) - 1/2                  #Function Set Up
    dFunc = lambda x: -np.exp(x)/math.pow(np.exp(x)+1,2)    #First Derivative
    tol = 10**(-9)                                          #Tolerance
    root = 0                                                #Root of Funciton

    start = -5.0                                            #Variables for the interval [-5,5]
    end = 5.0
    points = 50000
    potentialGuess = np.linspace(start,end,num=points)      #Created 5000 points between -5 and 5


    valids = []
    for x in potentialGuess:                                #Iterating through each point in potentialGuess and saving all the points that coverged into an array
        if newtonMethod(func,dFunc,tol,x,root) is not None:
            valids.append((x, newtonMethod(func,dFunc,tol,x,root)))


    # Visuals - Printing out all the results
    if showVisuals:
        print("\n\n\n\n\n")

        print("Grid: \n Start: {}\n End: {} \n # of Points: {}\n".format(start,end,points))

        print("(Approx.) Lowest intial Guess that's valid is {}:\n With a Final Guess of: {}\n".format(valids[0][0],valids[0][1]))
        print("(Approx.) Highest intial Guess that's valid is {}:\n With a Final Guess of: {}\n".format(valids[len(valids)-1][0],valids[len(valids)-1][1]))
    return (valids[0][0],valids[len(valids)-1][0])


def extraCreditOne():
    orignalFunc = lambda x: 1/(np.exp(x)+1) - 1/2
    intevals = hwHelper(True)
    x = np.linspace(intevals[0],intevals[1],num=1000)
    y = orignalFunc(x)
    

    xw = np.arange(-5,6)
    yw = orignalFunc(xw)
    line2, = plt.plot(xw,yw,color = "blue",label="Original Function")
    line1, = plt.plot(x,y,color = "red",label="Original Function -  With Intervals")
    plt.xlabel("X-Values")
    plt.ylabel("Y-Values (Function Output)")
    plt.title("Function: \"1/(e^x + 1) - 0.5\" for the intervals \nwhere Newton's Method Converges")
    plt.legend(handles=[line1,line2])
    plt.show()


# hwHelper(True)
extraCreditOne()