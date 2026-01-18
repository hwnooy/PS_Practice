import sys
import math
from collections import deque
input = sys.stdin.readline
prog = list(map(int, input().split()))
speed = list(map(int, input().split()))

def solution(progresses, speeds):
    temp = []
    answer= []
    for k in range(len(progresses)):
        temp.append(math.ceil((100-progresses[k])/speeds[k]))
    dq = deque(temp)

    
    
    while dq : # 비어있지않는 동안 
        curr = dq.popleft()
        work=1
        # 맨앞보다 작으면 다 가져오기 (기준은 완전 그냥 맨앞이 기준임.)
        while dq and curr >= dq[0]:
            dq.popleft()
            work+=1
        # while문을 빠져나오면, 즉 맨앞보다 이제 큰 수가 나오면 배포개수 카운트 끝 
        answer.append(work)
        #curr = dq.popleft()
        
        
    return answer