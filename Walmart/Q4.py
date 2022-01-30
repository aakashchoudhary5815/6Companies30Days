class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        #code here
        ans, x, y = 1, a+b-2, min(a,b)-1
        for i in range(1,y+1):
            ans = ans*(x-y+i)/i
        return int(ans)