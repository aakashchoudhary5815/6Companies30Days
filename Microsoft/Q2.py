from collections import defaultdict
class Solution:
    def cycle(self,visited,arr,i,rec):
        visited[i]=True
        rec[i]=True
        for j in arr[i]:
            if visited[j]==False:
                if self.cycle(visited,arr,j,rec)==True:
                    return True
            elif rec[j]==True:
                return True
        rec[i]=False
        return False
    def isPossible(self,N,prerequisites):
        #code here
        visited=[False]*N
        rec=[False]*N
        arr=defaultdict(list)
        for i in range(0,len(prerequisites)):
            arr[prerequisites[i][1]].append(prerequisites[i][0])
        for i in range(0,N):
            if self.cycle(visited,arr,i,rec)==True:
                return 0
        return 1