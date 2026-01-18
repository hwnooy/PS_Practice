import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n < m :
    print(2*n+1)
elif n>m:
    print(2*m+1)
elif n==m : print(n+m)