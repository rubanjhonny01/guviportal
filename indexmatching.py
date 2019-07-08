n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in range(len(l)):
    if i==l[i]:
        l1.append(i)
if l1!=[]:
    for x in l1:
        print(x,end=" ")
else:
    print('-1')
