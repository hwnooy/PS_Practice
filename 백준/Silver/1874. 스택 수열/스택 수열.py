import sys
input = sys.stdin.readline
n = int(input())
ans=[int(input()) for _ in range(n)]

'''for k in range(n):
    num=int(input())
    ans.append(num)'''

dump=[]
results=[]
now = 1 # 넣을 숫자 포인터 느낌 중요
possible = True  # 판단 변수 

for num in ans: # 굳이 while True로 여러번할 필요X 
    # 목표 숫자에 도달할떄까지 now 푸쉬
    while now<=num:
        dump.append(now)
        results.append("+")
        now+=1
    
    # 도달하면 pop하기 (while문 탈출)
    if dump[-1]==num:
        dump.pop()
        results.append("-")
    else :
        possible=False
        break
                
if possible:
    print("\n".join(results))
else:
    print("NO")