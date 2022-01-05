def CountWays(self, str):
	# Code here
    if str == '0':
        return 0
    if len(str) <= 1:
        return 1
    if str[0] == '0' or '00' in str:
        return 0
    d = [1 for i in range(len(str)+1)]
    for j in range(2, len(str)+1):
        (d1, d2) = (int(str[j-2]), int(str[j-1]))
        if d1 > 0 and d2 > 0:
            if d1*10+d2 < 27:
                d[j] = d[j-1] + d[j-2]
            else:
                d[j] = d[j-1]
        else:
            if d1 == 0:
                d[j] = d[j-1]
            else:
                if d1 > 2:
                    return 0
                else:
                    d[j] = d[j-2]
    return d[-1] % (10**9 + 7)