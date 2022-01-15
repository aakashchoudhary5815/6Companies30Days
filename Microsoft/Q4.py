def spirallyTraverse(self,matrix, r, c): 
    # code here 
    res = []
    t, d, l, r,dirs = 0, r-1, 0, c-1, 0
    while t<=d and l<=r:
        if dirs == 0:
            for i in range(l,r+1,1):
                res.append(matrix[t][i])
            t+=1
        elif dirs == 1:
            for i in range(t,d+1,1):
                res.append(matrix[i][r])
            r-=1
        elif dirs == 2:
            for i in range(r,l-1,-1):
                res.append(matrix[d][i])
            d-=1
        elif dirs == 3:
            for i in range(d,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        dirs = (dirs+1)%4
    return res