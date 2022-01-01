def gcdOfStrings(self, str1: str, str2: str) -> str:
    res, s = [], ""
    
    for i in range(len(str1)):
        s += str1[i]
        if s*(len(str1) // len(s)) == str1 and s*(len(str2) // len(s)) == str2:
            res.append(s)
    if res == []:
        return ""
    return res[-1]