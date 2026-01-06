import sys
input = sys.stdin.readline
n = int(input())
# vps 올바른 괄호 ,
for k in range(n):
    is_vps=True
    line=input().strip()
    check=[]
    for l in line:
        #print("l= "+str(l))
        if l=='(':
            check.append(l)
        elif l==')':
            if len(check)!=0:
                if check and check[-1] =='(':
                    check.pop()
            else:
                is_vps=False  # 여는 괄호가 존재하고나서 이것이 있어야 vps
                break

    if is_vps and len(check)==0: # 다 없어지기도해야 
        print("YES")
    else:
        print("NO")

