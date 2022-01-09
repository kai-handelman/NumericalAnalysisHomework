import numpy as np
from numpy.linalg import matrix_rank
from numpy.linalg import svd
from numpy.linalg import cond
from numpy.linalg import solve
import matplotlib.pyplot as plt

def readFile(fileName):
    returnContent = []
    with open(fileName,'r') as f:
        contents = f.readlines()
        for i in contents:
            returnContent.append(i.split(","))
        for i in returnContent:
            i[len(i)-1] = i[len(i)-1].replace("\n","")

        return returnContent

def helper():
    print("\n\n\n\n")

def getTranspose(matrix):
    tMatrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tMatrix[j][i] = matrix[i][j]
    return tMatrix

def isSymmetrical(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    tMatrix = getTranspose(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != tMatrix[i][j]:
                # print(i,j)
                # print(matrix[i][j])
                # print(tMatrix[i][j])
                # print(matrix[j][i])
                return False
    return True

def isDiagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i != j and matrix[i][j] != 0:
                return False
    return True

def isOrthogonal(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    tMatrix = getTranspose(matrix)                                                      #Transposed Matrix   
    rMatrix = np.matmul(matrix,tMatrix)                                                 #Result Matrix
    for i in range(len(matrix)):
        if rMatrix[i][i] != 1:
            return False
    return isDiagonal(rMatrix)

def getSVD(matrix):
    u,s,h = svd(matrix)
    return min(s),max(s)
    
def generateRight(matrix):
    n = len(matrix)
    m = 1
    b = []
    for i in range(5):
        b = np.random.rand(n,m)
        try:
            x = solve(matrix,b)
            # print("{}. b = {}".format(i+1,b))
            # print("X found: {}".format(x))
        except:
            print("\nError - Couldn't find a valid x")
            return
    print("No problem finding a solution 5 randomly generated right-hand-sides (i.e. b)")
    
def nonZeroGraph(matrix):
    plt.spy(matrix,markersize='3')
    plt.grid('on')
    plt.title("Non-Zero Elements")
    plt.xlabel("col")
    plt.ylabel("row")
    plt.show()
   
def magHeatMap(matrix):
    plt.imshow(abs(matrix),cmap="hot",interpolation='nearest')
    plt.title("Magnitude of Elements")
    plt.xlabel("col")
    plt.ylabel("row")
    plt.colorbar()
    plt.show()
    
    pass           


def mainHwFunction(fileName):
    contents = readFile(fileName)
    print("Data for: " + fileName)
    print("Matrix Dimentions : {} by {}".format(len(contents),len(contents[0])))        #Q1: Matrix Dimensions
    matrix = np.array(contents,dtype=float)
    print("Number of Non Zero Elements: {}".format(len(matrix[matrix != 0])))           #Q2: Zero Elements    
    print("Is Symmetrical: {}".format(isSymmetrical(matrix)))                           #Q3: Symmetry
    print("Is Diagonal: {}".format(isDiagonal(matrix)))                                 #Q4: Diagonal
    print("Is Orthogonal: {}".format(isOrthogonal(matrix)))                             #Q5: Orthogonal
    print("Rank of Matrix: {}".format(matrix_rank(matrix)))                             #Q6: Rank
    min,max = getSVD(matrix)
    print("Smallest Singular Value: {} \nLargest Singular Value: {}".format(min,max))   #Q7&8: SVD
    print("Condition Number: {}".format(cond(matrix)))                                  #Q9: Condition Number
    generateRight(matrix)                                                               #Q10: Solving for a random b  (Ax = b)
    nonZeroGraph(matrix)
    magHeatMap(matrix)



mainHwFunction("mat5.txt")
