def fourSum(self, arr, k):
    # code here
	
	ans=[]
    # sort the array
    arr.sort()
    n=len(arr)
    
    # pick two elements from loop
    for i in range(n-3):
        for j in range(i+1, n-2):
            left=j+1
            right=n-1
            # pick two elements using two-pointer
            while left<right:
                s=arr[i]+arr[j]+arr[left]+arr[right]
                if s==k:
                    # we found one quadruple
                    res=[arr[i], arr[j], arr[left], arr[right]]
                    res.sort()
                    if res not in ans:
                        ans.append(res)
                    left+=1
                    right-=1
                elif s<k:
                    left+=1
                else:
                    right-=1
    return ans