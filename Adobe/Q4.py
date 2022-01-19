def equalPartition(self, N, arr):
    # code here
    summ = sum(arr)
    if summ % 2 != 0:
        return False
    else:
        t = summ // 2
        d = [[0 for i in range(t+1)] for j in range(N+1)]
        for i in range(N+1):
            for j in range(t+1):
                if i == 0:
                    d[i][j] = False
                if j == 0:
                    d[i][j] = True
        for i in range(1,N+1):
            for j in range(1,t+1):
                if arr[i-1] <= j:
                    d[i][j] = d[i-1][j-arr[i-1]] or d[i-1][j]
                else:
                    d[i][j] = d[i-1][j]
    return d[N][t]