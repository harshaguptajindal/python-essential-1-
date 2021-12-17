y=int(input("give me a year"))
if y<1582:
    print("not in gregorian calender")
elif y%4:
    print("common year")
elif y%100:
    print("leap year")
elif y%400:
    print("common year")
else :
    print("leap year")
    
