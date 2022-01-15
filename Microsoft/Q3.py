import numpy as np
def rotate(matrix): 
    #code here
    res = np.transpose(matrix)
    res = res[::-1]
    for i in range(len(res)):
        for j in range(len(res)):
            matrix[i][j] = res[i][j]