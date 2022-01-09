import math
import matplotlib.pyplot as plt

def bisection(f, tol, a,b,target):
    error = []
    temp = None
    if f(a) * f(b) < 0:
        while abs((b-a) /2) > tol:
            temp = (a+b)/2
            if f(temp) == 0:
                return temp
            elif f(a) * f(temp) < 0:
                b = temp
            else:
                a = temp
            error.append(abs(target-temp))
        return ((a+b)/2,error)
    return (temp,error)

def fixedPoint(f, x, curTol, diffTol, M,target):
    error = []
    for b in range(M):
        temp = f(x)
        if curTol > abs(f(x)) or diffTol > abs(f(temp) - f(x)):
            return (x,b,error)
        x = temp
        error.append(abs(target-temp))
    return (x,M,error)


# For part 5
targetRoot = (3+math.sqrt(57))/8
func = lambda x: 4*(x**2) - 3*x -3
a = 1
b = 3
tol = 10**-4
(_,biErrors)=bisection(func,tol,a,b,targetRoot)

func = lambda x: ((3*(x**2)+3*x)/4)**(1./3)
x = 2
cT = 10**-4         #Tolerance of Error
cD = 10**-8         #Tolerance of Difference in Iteration
maxIter = 100
(_,_,fiError) = fixedPoint(func,x,cT,cD,maxIter,targetRoot)

biErrors = biErrors[0:15]
fiError = fiError[0:15]


line1,=plt.plot(biErrors,label="Bisection Method")
line2,=plt.plot(fiError,label="Fixed Point Method")
plt.title("For Positive Root of f(x): {}".format(targetRoot))
plt.legend(handles=[line1,line2])
plt.xlabel("Num of Iterations")
plt.ylabel("Error Value")
plt.show()



print(biErrors)
# # For bisection
# func = lambda x: 4*(x**2) - 3*x -3
# a = 1
# b = 2
# tol = 10**-4
# print("Start Interval: {}".format(a))
# print("End Interval: {}".format(b))
# print("Tolerance: {}".format(tol))
# print("Result from Bisection Method: {}".format(bisection(func,tol,a,b)))



# For fixedPoint
# t = 1/3
# func = lambda x: ((3*(x**2)+3*x)/4)**(1./3)
# temp = (3-math.sqrt(57))/8
# # print(temp)
# # print(func(temp))
# x = 0.1
# cT = 10**-4
# cD = 10**-8
# m = 5000
# print("Intital x_0 Guess: {}".format(x))
# print("Max Iterations Allowed: {}".format(m))
# print("Tolerance of Error: {}".format(cT))
# print("Tolerance of Difference in Iteration: {}".format(cD))
# r =fixedPoint(func,x,cT,cD,m,0)
# print("Iterations took: {}\nResult: {}".format(r[1],r[0]))





