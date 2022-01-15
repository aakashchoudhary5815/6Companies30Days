def possibleWords(self,a,N):
    #Your code here
    d = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    def helper(i,word,res):
        if i == N:
            res.append(''.join(word))
            return
        for val in d[a[i]]:
            word.append(val)
            helper(i+1,word,res)
            word.pop()
    res = []
    helper(0,[],res)
    return res