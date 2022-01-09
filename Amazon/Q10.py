def matchPairs(self,nuts, bolts, n):
	# code here
	
	res = ['!', '#', '$', '%', '&', '*','@','^', '~']
	ans = set()
	for i in nuts:
	    ans.add(i)
	nuts.clear()
	bolts.clear()
	for i in res:
	    if i in ans:
	        nuts.append(i)
	        bolts.append(i)