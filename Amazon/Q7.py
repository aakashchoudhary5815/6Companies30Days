def FirstNonRepeating(self, A):
	# Code here
    res = []
    inList = [] * 256
    repeat = [False] * 256
    for i in range(len(A)):
        temp = A[i]
        if not repeat[ord(temp)]:
            if not temp in inList:
                inList.append(temp)
            else:
                inList.remove(temp)
                repeat[ord(temp)] = True
        if len(inList) != 0:
            res.append(inList[0])
        else:
            res.append("#")
    ans = ''.join(res)
    return ans