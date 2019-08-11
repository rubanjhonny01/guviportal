n,a,b=map(int,input().split())
sum1=0
i=2
j=2
if n%(a+b)==0:
    print("YES")
else:
    a1="NO"
    while sum1<=n:
        while sum1<=n:
            sum1=(a*i)+(b*j)
            if sum1==n:
                a1="YES"
                break
            i+=2
        j+=2
        i=2
    print(a1)
        
