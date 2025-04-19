s=0
n=int(input("Enter a value:"))
for i in range (1, n+1):
    f=1
    for j in range(1, i+1):
        f=f*j #f=1 then f*j=1*1=1
        s=s+f # 0+1=1
        print("Sum of factorial series=",s)