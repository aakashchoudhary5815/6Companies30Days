def subArraySum(self,arr, n, s): 
    #Write your code here
    summ, i, j = 0, 0, 0
    while j < n:
        summ += arr[j]
        if summ < s:
            j += 1
        elif summ == s:
            return [i+1, j+1]
        else:
            while summ > s:
                summ -= arr[i]
                i += 1
            if summ == s:
                return [i+1, j+1]
            j += 1
    return [-1]