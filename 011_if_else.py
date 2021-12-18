i=float(input("enter your income: "))
if i<=85528:
    tax=(0.18*i)-556.2
    if tax<0:
        tax = 0
    print("this is your", tax, "amount to be paid")
else:
    tax=14839+(0.32*(i-85528))
    print("this is your", tax, "amount to be paid")

