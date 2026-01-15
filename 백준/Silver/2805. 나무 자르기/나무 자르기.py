import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cut=list(map(int,input().split()))

cut.sort()

def check(left, right):
    ans=0
    while left<=right:
        #print(f"left is {left} and right is {right}")
        
        #mid = int((left+right)/2) # 높이의 시작
        mid = (left+right)//2  # 몫 처리는 작대기 2개
        cutSum=0
        for i in cut:
            if i>mid:
                cutSum=cutSum+(i-mid)      
        # check 변수를 없애려면 for문 밖에서 처리하면 됨!!!
        # 길이가 너무 길면 left값이 더 커져야 높이가 크게 됨 
        # 근데 짧은거보단 긴게 나음 
        
        if cutSum>=m:
            # 아래 주석은 다시 풀면서 얻은 지식 
            # 1. m미터 이상 확보했으므로 '일단 성공' <- m미터 이상 확보시 일단 성공 하는거 캐치해야
            # 2. 더 높게 자를 수 있는지 확인하기 위해 오른쪽 탐색, 오른쪽 탐색은 왼쪽을 늘리는 것 
            ans = mid 
            left = mid+1
        else:
            # 나무가 모자른 케이스 -> 왼쪽 탐색해야, 왼쪽탐색은 끝을 줄이는 것 
            right = mid -1
    return ans
           # print(f"cutSum is {cutSum}")
           
result = check(0, cut[-1])
print(result)