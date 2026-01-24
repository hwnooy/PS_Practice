import sys
input = sys.stdin.readline

def oposite(word):
    # 태그 안의 문자열인지 체크해야함 - 이거 놓침
    in_tag = False
    stack=[]
    # 갑자기 스택에 그대로 넣고 출력하면 되겟다햇는데 캐치 오래걸림 - 나는 태그때문에 스택생각
    # 스택의 LIFO 특성으로 인해 pop하면 그냥 그대로 반대로 출력될 수 있음 놓침 
    
    for w in word:
        if w=='<':
            # 만났을때 그 앞에 있는것들 처리 아하!
            while stack:
                print(stack.pop(), end="")
            # 스택에 있는거 다 출력하고 태그 안에꺼 처리 
            #in_tag = True
            print(w, end="")
            in_tag = True
            
        elif w=='>':
            print(w, end="")
            in_tag = False
            
            # 이거는 뭐 앞에 있는거 신경쓸 필요 없음 닫기만
        
        # 여기서 in_tag 여부에 따른 문자열 출력
        elif in_tag:
            print(w, end="")
            
        # in flag이 false이면 
        else:
            if w==' ':
                while stack:
                    print(stack.pop(), end='')
                print(w, end='')
            
            # 단어일떄 
            else:
                stack.append(w)
    while stack:
        print(stack.pop(), end='')


line = input().rstrip()
oposite(line)