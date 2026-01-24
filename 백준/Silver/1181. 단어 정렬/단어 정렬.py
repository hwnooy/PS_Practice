import sys
input = sys.stdin.readline
n = int(input())
line = [0]*51
lined = {}
for k in range(n):
    word = input().rstrip()
    lined[word]= len(word)

sortArr = sorted(lined.items(), key = lambda x: (x[1], x[0]))
#print(sortArr)
for k in sortArr:
    #for (a,b) in k:
    print(k[0])