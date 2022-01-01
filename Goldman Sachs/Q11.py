def findTwoElement( self,arr, n): 
    # code here
    d = {}
    m, r = 0, 0
    for i in range(1,n+1):
        d[i] = 0
    for e in arr:
        d[e] = d.get(e,0)+1
    for k in d:
        if d[k] == 0:
            m = k
        elif d[k] > 1:
            r = k
    return r,m