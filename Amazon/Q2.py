def longestMountain(self, arr: List[int]) -> int:
    maxx = 0
    i = 1
    while i<len(arr)-1:
        peak = arr[i]>arr[i-1] and arr[i]>arr[i+1]
        if not peak:
            i += 1
            continue
        j = i-2
        while(j >= 0 and arr[j]<arr[j+1]):
            j -= 1
        k = i+2
        while(k < len(arr) and arr[k]<arr[k-1]):
            k += 1
        c = k-j-1
        if(c>maxx):
            maxx = c
        i = k
    return maxx