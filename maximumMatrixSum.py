## this code finds the maximum sum in a given matrix, when two rows are selected and both multiplied by -1


def transpose(m):
    #imput matrix is m X n
    rowlength = len(m)
    columnlength = len(m[0])
    #for transpose matrix, columnlength of original matrix become the row length(numbe of list in the array) 
    #of the transpose matrix
    transposematrix = [None]*columnlength
    #creating column for the transpose matrix
    for row in range(columnlength):
        #the column length for transpose matrix is the rowlength of the original matrix
        transposematrix[row] = [None]*rowlength
    for row in range(rowlength):
        for column in range(columnlength):
            transposematrix[column][row] = m[row][column]
    
    return transposematrix

def matrixSum(matrix):
    
    if(len(matrix)<2 and len(matrix[0])<2):
        print("a unit element matrix")
        print(matrix[0][0])
        return matrix[0][0]
    
    if(len(matrix[0])<2):
        matrix = transpose(matrix)
        maxiMatrixSum = list(map(sum, matrix))[0]
        print(maxiMatrixSum)
        return maxiMatrixSum
        #matrix = transpose(matrix)[0]
        #print(matrix)
        #summatrix = sum(matrix)
        #print(summatrix)
        #return k
    else:
        matrixsum = 0
        #print(matrix)
        matrix = transpose(matrix)
        sumrow = list(map(sum, matrix))
        print(sumrow)
        for index in range(2):

            minum = min(sumrow)
            #print(minum)
            matrixsum += (minum * -1)
            #print(matrixsum)
            del sumrow[sumrow.index(minum)]

        matrixsum = sum(sumrow) + matrixsum
        maxiMatrixSum = matrixsum
        print(maxiMatrixSum)
        return maxiMatrixSum
        
    
matrix = [[1, 8, 10, 13]]
matrixsum = matrixSum(matrix)
