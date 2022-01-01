def encode(arr):
    # Code here
    prev, res, c = arr[0], '', 1
    for i in range(1,len(arr)):
        if prev == arr[i]:
            c += 1
        else:
            res += prev + str(c)
            prev = arr[i]
            c = 1
    res += prev + str(c)
    return res