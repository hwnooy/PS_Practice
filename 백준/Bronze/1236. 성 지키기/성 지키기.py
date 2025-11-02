import sys
input = sys.stdin.readline
n, m = map(int, input().split())
result = []
answer1 = 0
answer2 = 0
for k in range(n):
    row = list(map(str, input().strip()))
    result.append(row)

for item in result:  # 행 체크 
    if 'X' not in item:
        answer1+=1

# 열 별로 체크 안해서 문제발생..
for j in range(m):
    flag = True
    for _ in range(n):
        if result[_][j] == 'X':
            flag=False
            break
        else :
            flag = True
            
    if (flag) :
        answer2+=1


if(answer1>answer2) :
    print(answer1)
else :
    print(answer2)
