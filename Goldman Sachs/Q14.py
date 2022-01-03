def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    res = 999999
    l, s = 0, 0
    for i in range(len(nums)):
        s+= nums[i]
        while s >= target:
            res = min(res, i-l+1)
            s -= nums[l]
            l += 1
    return res if res < 999999 else 0