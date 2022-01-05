from collections import defaultdict
def canPair(self, nums, k):
	# Code here
	if len(nums) & 1:
	    return 0
	freq = defaultdict(lambda: 0)
	for i in range(0, len(nums)):
	    freq[((nums[i]%k)+k)%k] += 1
	for i in range(0, len(nums)):
	    rem = ((nums[i] % k) + k) % k
	    if 2*rem == k:
	        if freq[rem] % 2 != 0:
	            return 0
	    elif rem == 0:
	        if freq[rem] & 1:
	            return 0
	    
	    elif freq[rem] != freq[k-rem]:
	        return 0
	return 1