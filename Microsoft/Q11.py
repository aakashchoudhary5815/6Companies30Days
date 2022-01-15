def generate(N):
    # code here
    res = []
    ans = ""
    for i in range(1,N+1):
        a = i
        while a:
            b = a%2
            ans = str(b) + ans
            a//=2
        res.append(ans)
        ans = ""
    return res