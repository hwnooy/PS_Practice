import sys
input = sys.stdin.readline
n = int(input())
sortArr=[0]*10001
for k in range(n):
    num = int(input())
    sortArr[num]+=1

for i in range(len(sortArr)):
    if sortArr[i]!=0:
        for _ in range(sortArr[i]):
            print(i)