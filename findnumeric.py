x=input()
y='1234567890'
for i in y:
  if i in x:
    x.remove(i)
if x!="":
  print("yes")
else:
  print("no")
