n = int(input())
a=[int(i) for i in input().split()]
a = sorted(a)
s = 0
for i in range(n//2+1):
    s+=a[i]//2+1
print(s)