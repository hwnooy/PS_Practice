import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))

def sol(arr, k):
    max_val = sum(arr[:k]) #앞에서부터 k개
    answer = max_val
    n = len(arr)
    for i in range(n-k):
        max_val = max_val - arr[i]+arr[i+k]
        answer = max(max_val, answer)
    return answer
        
print(sol(arr,k))
            