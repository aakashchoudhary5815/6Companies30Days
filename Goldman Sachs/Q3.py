def countSubArrayProductLessThanK(self, a, n, k):
    #Code here
    c, p, l = 0, 1, 0
    for r in range(n):
        p*=a[r]
        while p >= k:
            p//= a[l]
            l+=1
        c+=1+(r-l)
    return c