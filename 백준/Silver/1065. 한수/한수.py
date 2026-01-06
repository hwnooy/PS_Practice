import sys
input = sys.stdin.readline

n = int(input())
ans=0
for k in range(1, n+1):
    # 11 22 33 44 55 66 77 88 99 100 101 102 103 104
    # 100 101 102 103 104 105 106 107 108 109 110
    if k<100 : ans+=1
    elif k>=100:
        #print("k번째 수 ", k, ":", k//100, (k%100)//10, k%10)
        # 모든 자리수가 같을때, 백과 일의자리 같을때  
        if k//100 == (k%100)//10 :
            if (k%100)//10 == k%10 :
                #print(k)
                ans+=1
        #elif k//100 == k%10:  171 이런거는 등차수열이 아니어서
         #   print(k)
          #  ans+=1
        elif k//100 - (k%100)//10 == (k%100)//10 - k%10:
           # print(k)
            ans+=1
            
print(ans)
        
