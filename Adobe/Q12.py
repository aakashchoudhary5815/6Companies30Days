def leaders(self, A, N):
    #Code here
    ans, maxx = [], -9999
    for i in reversed(A):
        if i >= maxx:
            maxx = i
            ans.append(maxx)
    return ans[::-1]