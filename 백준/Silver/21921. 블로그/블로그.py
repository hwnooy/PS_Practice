import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

tempSum=sum(arr[0:x])# x개 합
# record에 미리 첫 값 넣기
record = [tempSum]
#print("first sum is ", tempSum)
pivot = tempSum
for k in range(x,n): # x부터 n-1까지 
    tempSum=tempSum-arr[k-x]+arr[k] # 첫값 빼고 x인덱스부터 더하기
    record.append(tempSum)

result = max(record)
if result ==0:
    print("SAD")
else:
    print(max(record))
    print(record.count(result))