n,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(q):
  x,y=map(int,input().split())
  f=l[x-1:y]
  print(sum(f))
