def lastPosition(N, M, K):
     
    if (M <= N - K + 1):
       return M + K - 1

    M = M - (N - K + 1)

    if(M % N == 0):
        return N
    return M % N