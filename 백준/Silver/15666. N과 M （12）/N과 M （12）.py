import sys
N, M =map(int, input().split())

N_list= list(map(int,sys.stdin.readline().split()))
N_list.sort()
result=[]

def DFS(a):
    if len(result)==M:
        print(*result)
        return
    remember=0
    for i in range(a, N):
        if remember != N_list[i]:
            result.append(N_list[i])
            remember=N_list[i]
            DFS(i)
            result.pop()
    
DFS(0)