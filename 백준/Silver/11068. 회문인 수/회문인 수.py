import sys
input = sys.stdin.readline
DigitNum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

tc = int(input())
def isDoor(base, num):
    na=[]
    while num!=0:
        na.append(DigitNum[num%base])
        num=num//base
    return ''.join(reversed(na))  

def isPal(arr):
    return arr==arr[::-1]

for k in range(tc):
    n = int(input())
    flag=False
    for k in range(2,65):
        toBase = isDoor(k,n)
        if (isPal(toBase)):
            flag=True
            #print(toBase)
            break
    if (flag):
        print(1)
    else:
        print(0)
    