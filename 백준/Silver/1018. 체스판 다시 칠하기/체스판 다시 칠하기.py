import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
result=[]
#8*8이 핵심
for i in range(n-7):
    for j in range(m-7):
        draw1=0 #w로 시작시 고쳐야
        draw2=0 #b로 시작시 고쳐야
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 인덱스 합의 짝/홀을 이용하면 체스판 패턴을 쉽게 판별 가능
                if (x+y)%2 ==0 :
                    if arr[x][y]!='W': draw1+=1
                    if arr[x][y]!='B': draw2+=1
                else:
                    if arr[x][y]!='B': draw1+=1
                    if arr[x][y]!='W': draw2+=1
        result.append(draw1)
        result.append(draw2)
        
print(min(result))