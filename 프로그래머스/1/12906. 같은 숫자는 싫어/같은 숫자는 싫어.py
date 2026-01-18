import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

def solution(arr):
    answer=[]
    for k in arr:
        if len(answer)==0:
            answer.append(k)
        elif answer and answer[-1] != k:
            answer.append(k)
    return answer