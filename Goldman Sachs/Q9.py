from collections import deque
def printMinNumberForPattern(self,seq):
    # code here 
    if not seq or not len(seq):
        return seq
    result = ''
    stack = deque()
    for i in range(len(seq) + 1):
        stack.append(i + 1)
        if i == len(seq) or seq[i] == 'I':
            while stack:
                result += str(stack.pop())

    return result