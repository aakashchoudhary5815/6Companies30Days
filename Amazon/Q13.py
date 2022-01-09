def orangesRotting(self, grid: List[List[int]]) -> int:
    f, r = [], []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                f.append([i,j])
            elif grid[i][j] == 2:
                r.append([i,j])
    mins = 0
    dirs = [[0,1],[1,0],[0,-1],[-1,0]]
    
    while len(f) > 0:
        temp = []
        
        for k in r:
            i1 = k[0]
            j1 = k[1]
            
            for d in dirs:
                i2 = i1+d[0]
                j2 = j1+d[1]
                
                if [i2,j2] in f:
                    f.remove([i2,j2])
                    temp.append([i2,j2])
        if len(temp) == 0:
            return -1
        
        r = temp
        mins += 1
    return mins