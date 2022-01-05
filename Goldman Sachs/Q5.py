import heapq
def getNthUglyNo(self,n):
	# code here
	d, res, c = {}, [], 0
	heapq.heappush(res,1)
	d[1] = 1
	while c!=n:
	    temp = heapq.heappop(res)
	    c += 1
	    if c == n:
	        return temp
	    if temp * 2 not in d:
	        d[temp*2] = 1
	        heapq.heappush(res, temp*2)
	    if temp * 3 not in d:
	        d[temp*3] = 1
	        heapq.heappush(res, temp*3)
	    if temp * 5 not in d:
	        d[temp*5] = 1
	        heapq.heappush(res, temp*5)
	return heapq.heappop(res)