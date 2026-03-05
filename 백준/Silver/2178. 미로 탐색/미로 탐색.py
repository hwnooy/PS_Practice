import sys
from collections import deque 
input = sys.stdin.readline


n, m = map(int, input().split())
arr = deque([list(input().strip()) for _ in range(n)])

def bfs(start, graph):
    # 시작점 큐에 넣기
    visited=[[0]*m for _ in range(n)]
    visited[0][0]=1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    answer=0
    queue = deque([start])
    #visited[start[0]][start[1]]=True
    
    while queue:
        # 큐에서 하나씩 꺼내기
        x,y = queue.popleft()
        
        if x==n-1 and y==m-1:
            return visited[x][y]
        
        # 연결된 노드들 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and arr[nx][ny]=='1':
                    visited[nx][ny]=visited[x][y]+1
                    queue.append((nx, ny))


result = bfs((0,0),arr)
print(result)