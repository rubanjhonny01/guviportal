n=int(input())
l=[]
le=[]
for i in range(n):
  l.append(input())
  le.append(len(l[i]))
o=min(le)
s=""
for i in range(o):
  count1=0
  for j in range(len(l)-1):
    if l[j][i]==l[j+1][i]:
      count1+=1
  if count1==n-1:
    s+=l[j][i]
print(s)
