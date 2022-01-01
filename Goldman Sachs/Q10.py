def kLargest(self,li,n,k):
    # code here
    li.sort()
    ans = []
    for i in range(n-k,n):
        ans.append(li[i])
    ans.sort(reverse = True)
    return ans