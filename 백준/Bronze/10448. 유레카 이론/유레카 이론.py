import sys
input = sys.stdin.readline
n = int(input())
tri_num = []
for k in range(1,1000):
    num = (k*(k+1))/2
    if num<=1000:
        tri_num.append(num)
    else :
        break

# 만들어진 삼각수로 num이 표현이 되는가 함수로   
def checkTriNum(num):    
    for i in tri_num:
        for j in tri_num:
            for k in tri_num:
                if i+j+k==num:
                    return True
    return False
                    

for k in range(n):
    num = int(input())

    if checkTriNum(num):
        print(1)
    else : 
        print(0)