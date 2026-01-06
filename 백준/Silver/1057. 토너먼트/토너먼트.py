import sys
input = sys.stdin.readline
    
num, a, b = map(int, input().split())
def sol(a,b):
    ans=0

    while True:
        if a==b:  
            break
        
        if a%2==0: a//=2
        else: a=a//2+1
        
        if b%2==0: b//=2
        else : b=b//2+1
        
        ans+=1
    
    return ans

print(sol(a,b))    