n=int(input())
l1=list(input().split())
l=[]
for x in l1:
  if l1.count(x)==1:
    l.append(x)
for x in l:
  print(x)
