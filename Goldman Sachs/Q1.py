def Anagrams(self,words,n):
    temp = {}
    for i in words:
        res = "".join(sorted(i))
        if temp.get(res,0)==0:
            temp[res] = [i]
        else:
            temp[res].append(i)
    ans = []
    for j in temp:
        ans.append(temp[j])
    return ans
