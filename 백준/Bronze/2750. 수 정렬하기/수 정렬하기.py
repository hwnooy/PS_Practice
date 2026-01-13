import sys
input = sys.stdin.readline

n = int(input())

def bubble(arr):
    for k in range(len(arr)-1, 0, -1):
        #print("index K = " , k)
        for i in range(0,k):
           # print("index I = ", i)
            if arr[i]>arr[i+1]:
                tmp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=tmp
    return arr 

arr=[]
for k in range(n):
    num=int(input())
    arr.append(num)
arr2 = bubble(arr)

for k in arr2:
    print(k)
        
