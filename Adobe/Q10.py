from collections import Counter
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        d = Counter(arr)
        temp, d2 = 0, {}
        for k,v in d.items():
            if v > temp:
                temp = v
        for k,v in d.items():
            if v == temp:
                d2[k] = v
        l = []
        for i,v in d.items():
            if v == temp:
                l.append(i)
        res = sorted(l)[0]
        return [res, temp]