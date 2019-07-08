n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for x in l:
    if x not in l1:
        l1.append(x)
    elif x in l1 and x not in l2:
        l2.append(x)
if len(l2)!=0:
    for x in l2:
        print(x,end=" ")
else:
    print("unique")
