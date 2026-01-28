import sys
input = sys.stdin.readline
from collections import deque
n = int(input()) # 사진 틀 개수 = 후보수 
m = int(input()) # 전체 학생 총 추천횟수 
arr = list(map(int, input().split()))

ans = 0
dq = {}

for k in range(len(arr)):
    
    key = arr[k]
    
    if key in dq.keys():
        dq[arr[k]]+=1
        
    else :
        if len(dq)>=n:
            target = min(dq.items(), key = lambda x: x[1])[0]
            del dq[target]
        dq[arr[k]]=1

ans = sorted(dq.keys())
print(*ans)