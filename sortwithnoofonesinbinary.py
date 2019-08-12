n=int(input())
l1=list(map(int,input().split()))
l1.sort()
l1.reverse()
dic1={}
l=[]
for x in l1:
    s=''
    k=x
    while x!=1:
        if x%2==1:
            s+='1'
        x=x//2
    s+='1'
    if s not in l:
        l.append(s)
    dic1[k]=s
l.sort()
l.reverse()
for x in l:
    for y,v in dic1.items():
        if x==v:
            print(y)
