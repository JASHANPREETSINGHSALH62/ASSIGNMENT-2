s1=int(input("ENTER L1: "))
s2=int(input("ENTER L2: "))
s3=int(input("ENTER L3: "))

if s1>s2+s3 or s2>s1+s3 or s3>s1+s2:
    print("NO")
elif s1==0 or s2==0 or s3==0:
    print("NO")
else:
    print("YES")
