import sys
input = sys.stdin.readline

while True:
    check=[]
    balanced=True
    line = input().rstrip()
    
    if line=='.':
        break
    for l in line:
    
        if l == '(':
            check.append(l)
        elif l == '[':
            check.append(l)
        elif l==')':
            if check and check[-1]=='(':
                check.pop()
            else:
                balanced=False
        elif l==']':
            if check and check[-1]=='[':
                check.pop()
            else:
                balanced=False
            
    if balanced and len(check)==0:
        print("yes")
    else :
        print("no")