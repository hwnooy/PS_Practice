import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

pivot = 0
left, right = 0, n-1
minSum=float('inf')
ans = (0, 0)
while left<right:
    tempSum = arr[left]+arr[right]
    
    if abs(tempSum) < minSum:
        minSum=abs(tempSum)
        ans = (arr[left], arr[right])
        
    if tempSum>0:
        right-=1
    elif tempSum<0:
        left+=1
    else:
        break

print(*ans)