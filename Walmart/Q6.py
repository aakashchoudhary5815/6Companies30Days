class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        mod = 1000000007
        
        N %= mod
        
        if R == 0:
            return 1
        
        if R == 1:
            return N
            
        tmp = self.power(N, R // 2)
        res = (tmp * tmp) % mod
        
        if R % 2 != 0:
            res = (res * N) % mod
        
        return res