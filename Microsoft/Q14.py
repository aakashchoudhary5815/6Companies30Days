def minSteps(self, D):
    # code here
    st,s = 0, 0
    while True:
        s += st
        st += 1
        if s == D:
            return st-1
            break
        if s > D and (s-D)%2 == 0:
            return st-1
            break
    return 0