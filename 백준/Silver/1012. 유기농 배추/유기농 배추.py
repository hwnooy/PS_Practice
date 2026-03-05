import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

tc = int(input())

def dfs(x,y):
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
            
    # 이미 배추위치가 1인 곳을 들어왔음
    arr[x][y]=0
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==1:
                dfs(nx,ny)
    
for t in range(tc):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    
    for k in range(k):
        a, b = map(int, input().split())
        arr[b][a]=1
    
    count=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                dfs(i,j) # 여기로 돌아오면 한 덩어리가 끝남 
                count+=1
    print(count)