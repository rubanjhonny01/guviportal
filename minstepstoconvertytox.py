x,y=map(str,input().split())
l=len(x)>=len(y) and len(y)or len(x)
l1=len(x)>=len(y) and len(x)or len(y)
count1=0
for i in range(l):
  if x[i]==y[i]:
    count1+=1
print(l1-count1)
