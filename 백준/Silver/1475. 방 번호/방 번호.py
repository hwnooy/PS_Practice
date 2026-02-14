import sys
import math
input = sys.stdin.readline

n = input().strip()
count = [0]*10

for i in n:
    if i=='6' or i=='9':
        count[6]+=1
    else:
        count[int(i)]+=1
count[6] = math.ceil(count[6]/2)
print(max(count))