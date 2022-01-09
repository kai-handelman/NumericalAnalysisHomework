import numpy as np
import numpy.linalg as ln
import numpy.random as rn
from tabulate import tabulate
import matplotlib.pyplot as plt

def readFile(fileName):
    returnContent = []
    with open(fileName,'r') as f:
        contents = f.readlines()
        for i in contents:
            returnContent.append(i.split(","))
        for i in returnContent:
            i[len(i)-1] = i[len(i)-1].replace("\n","")
            for j in range(len(i)):
                i[j] = float(i[j])

        return returnContent

def getTranspose(matrix):
    tMatrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tMatrix[j][i] = matrix[i][j]
    return tMatrix

def normEq(a,b):
    aTa = np.dot(getTranspose(a),a)
    atB = np.dot(getTranspose(a),b) 
    try:
        r = ln.cholesky(aTa)
    except:
        print("Not positive definite")
        return None
    y = ln.solve(r,atB)
    return ln.solve(getTranspose(r),y)

def backSub(matrix,right):
    x = np.zeros_like(right,float)
    for i in range(len(matrix)-1,-1,-1):
        temp = right[i][0]
        for j in range(len(matrix[i])-1, i, -1):
            temp = temp - matrix[i][j] * x[j]
        x[i] = temp / (matrix[i][i])
    return x

def thinQR(a,b):
    q,r = ln.qr(a,mode='reduced')
    nB = np.dot(getTranspose(q), b)
    x = backSub(r,nB)
    return x

def generateRight(m,Count):
    bs = []
    for i in range(Count):
        bs.append(rn.rand(m,1))
    return bs

def problemTwo(tempA,b):
    # Part A
    trueX = []

    errNormalEq = []
    errQREq = []
    for i in tempA:
        x = ln.lstsq(i,b,rcond = -1)[0]
        trueX.append(x)

        ne_X = normEq(i,b)
        errNormalEq.append(ln.norm(ne_X-x)/ln.norm(x))

        ne_X = thinQR(i,b)
        errQREq.append(ln.norm(ne_X-x)/ln.norm(x))

    return  errNormalEq,errQREq

def main():
    matrix = np.array(readFile("mat1-2.txt"))
    # Question One
    kmin = 40
    kmax = 65
    kArrry = []
    pOneData = [["K","Size","Rank","Condition Number"]]
    kCon = []
    for i in range(kmin,kmax+1):
        tempMatrix = matrix[:,0:i]
        kArrry.append(tempMatrix)
        pOneData.append([i,str(len(tempMatrix))  + "x" + str(len(tempMatrix[0])), ln.matrix_rank(tempMatrix), ln.cond(tempMatrix)])
        kCon.append(ln.cond(tempMatrix))
    print(tabulate(pOneData,headers="firstrow",tablefmt='grid')+ "\n")

    # Question Two
    randomB = generateRight(len(matrix[0]),100)
    ne = []
    qr = []

    for i in randomB:
        neTemp,qrTemp = problemTwo(kArrry,i)
        ne.append(neTemp)
        qr.append(qrTemp)

    #Question Three
    avgErr = []
    neData = []
    qrData = []
    for i in range(26):
        tempSumQR = 0
        tempSumNE = 0
        for j in range(len(randomB)):
            tempSumQR = tempSumQR + qr[j][i]
            tempSumNE = tempSumNE + ne[j][i]
        avgErr.append([i+kmin,tempSumNE/26,tempSumQR/26])
        neData.append(tempSumNE/26)
        qrData.append(tempSumQR/26)


    pThreeData = [["K","NE Error Average","QR Error Average"]]
    pThreeData = pThreeData + avgErr
    print(tabulate(pThreeData,headers="firstrow",tablefmt='grid')+ "\n")



    # GRAPH MAKING
    xData = list(range(kmin,kmax+1))
    plt.xlabel("Number of Columns")
    plt.ylabel("Least Squares Error")
    plt.plot(xData,neData,'r',label="Normal Equation")
    plt.plot(xData,qrData,'b',label="QR Equation")
    plt.ylim([10**(-15), 1])
    plt.legend(loc="upper left")
    plt.show()

    plt.plot(xData,kCon,'b')
    plt.xlabel("Number of Columns")
    plt.ylabel("Condition Number")
    plt.ylim([np.power(10,2), np.power(10,8)])
    plt.show()

    
def test():
    a = np.array([[1,2,3],[2,2,2],[5,5,5]])
    print(a[0:2,0:2])

# test()
main()