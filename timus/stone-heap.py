
n = int(input())
ds = input().split(' ')
ns = []
for d in ds:
    ns.append(int(d))

m=0
end = 2**n
ms=1000000000
while m<end:
    i=a=b=0
    while i<n:
        if (1<<i) & m:
            a=a+ns[i]
        else:
            b=b+ns[i]
        i=i+1
    x=a-b
    s = -x if x<0 else x
    if(ms>s):
        ms=s
    m=m+1

print(ms)