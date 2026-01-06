import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
list1 = []
for num in range(1, n+1):
    list1.append(num)
    
q = deque(list1)
answer=[]
while len(q)>0:
    q.rotate(-k+1)
    answer.append(q.popleft())

print("<" + ", ".join(map(str, answer)) + ">")