c=0
n=int(input("enter the digit"))
for i in range(2,n//2+1):
    if n%i==0:
       c=c+1
    break
if c>0:
    print("composite")
else:print("prime")
print("the end")
