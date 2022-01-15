def calculateSpan(self,a,n):
    #code here
    stack = []
    stack.append(0)
    res = []
    res.append(1)
    for i in range(1,n):
        while len(stack) != 0 and a[stack[-1]] <= a[i]:
            stack.pop()
        if len(stack) == 0:
            res.append(i+1)
        else:
            res.append(i-stack[-1])
        stack.append(i)
    return res