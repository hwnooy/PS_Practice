import sys
from collections import deque
input = sys.stdin.readline
q = deque()

card=int(input())

for k in range(1, card+1):
    q.append(k)
    
## 맨 위에 있는게 인덱스 0, 맨 뒤에 있는게 마지막 수
while len(q)!=1:
    q.popleft()
    q.append(q.popleft())
print(q[0])