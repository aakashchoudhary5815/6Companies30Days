from collections import deque
def max_of_subarrays(self,arr,n,k):
    '''
    you can use collections module here.
    :param a: given array
    :param n: size of array
    :param k: value of k
    :return: A list of required values 
    '''
    #code here
    res = []
    dq = deque()
    for i in range(k):
        while dq and arr[i] > arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    for i in range(k,n):
        res.append(arr[dq[0]])
        while dq and dq[0] <= i-k:
            dq.popleft()
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    res.append(arr[dq[0]])
    return res