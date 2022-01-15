def FindMaxSum(self,a, n):
        
    # code here
    if n == 1:
        return a[0]
    p, q = 0, a[0]
    for i in range(2, n+1):
        r = max(q, p+a[i-1])
        p = q
        q = r
    return r