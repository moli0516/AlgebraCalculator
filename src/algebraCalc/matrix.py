"""
format: list(list(int))
"""

def add(a: list, b: list) -> list:
    if(len(a) != len(b) or len(a[0]) != len(b[0])):
        raise ValueError("The dimension of two matrix is not same.")
    else:
        newMatrix = []
        for i in range(len(a)):
            newMatrix.append([])
            for j in range(len(a[0])):
                newMatrix[i].append(a[i][j] + b[i][j])
        return newMatrix
    
#check the matrix is square matrix or not
def isSquare(a: list) -> bool:
    if(len(a) == len(a[0]) or len(a) == 1):
        return True
    return False

#help the multiplication function to add values
def sumOfArray(a: list, b: list, n: int) -> float:
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i][n]
    return sum

#transpose the matrix
def transpose(a: list) -> list:
    newMatrix = []
    for i in range(len(a[0])):
        newMatrix.append([])
        for j in range(len(a)):
            newMatrix[i].append(a[j][i])
    return newMatrix
    
def multiplication(a: list, b: list) -> list:
    """
    i, j
    [[x, x, x],       [[x, x, x],    [[x, x, x],
     [x, x, x],   *    [x, x, x], =   [x, x, x],
     [x, x, x],        [x, x, x]]     [x, x, x],
     [x, x, x]]                       [x, x, x],]
     
    """
    if(len(a[0]) != len(b)):
        raise ValueError("The number of column or the first matrix is not equal to the number of row of the second matrix.")
    else:
        newMatrix = []
        for i in range(len(a)):
            newMatrix.append([])
            for j in range(len(b[0])):
                newMatrix[i].append(sumOfArray(a[i], b, j))
        return newMatrix
    
def getCofactor(a: list, p: int, q: int) -> float:
    temp = []
    for i in range(len(a)):
        if(i != p):
            temp.append([])
        for j in range(len(a[0])):
            if(i != p and j != q):
                temp[len(temp) - 1].append(a[i][j])
    return (-1)**(p + q) * det(temp)

def det(a: list) -> float:
    if(isSquare(a)):
        if(len(a) == 1):
            return a[0]
        elif(len(a) == 2):
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]
        else:
            sum = 0
            for i in range(len(a[0])):
                sum += a[0][i] * getCofactor(a, 0, i)
            return sum
    
def adjoint(a: list) -> list:
    newMatrix = []
    for i in range(len(a)):
        newMatrix.append([])
        for j in range(len(a[0])):
            newMatrix[i].append(getCofactor(a, i, j))
    return transpose(newMatrix)

def inverse(a: list) -> list:
    newMatrix = adjoint(a)
    if(det(a) == 0):
        raise ValueError("The determinant of the matrix is 0, which the matrix is singular.")
    for i in range(len(a)):
        for j in range(len(a[0])):
            newMatrix[i][j] = 1 / det(a) * newMatrix[i][j]
    return newMatrix