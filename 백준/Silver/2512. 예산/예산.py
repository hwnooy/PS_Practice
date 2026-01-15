import sys
input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
maxCost = int(input())
req.sort()

def check(left, right):
    ans=0
    while left<=right:
        mid = (left+right)//2
        tempSum=0
        for money in req:
            if money <= mid :
                tempSum+=money
            else :
                tempSum+=mid
        
        if tempSum <= maxCost:
            ans = mid
           # money = mid
            left = mid+1
        else :
            right = mid-1
            
    return ans


if sum(req) <= maxCost:
    print(max(req))
else :
    localMax = check(0, req[-1])
    print(localMax)