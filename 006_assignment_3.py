hour=int(input("starting time in hours:"))
minute=int(input("starting time in minues:"))
duration=int(input("calculate duration in minutes"))
duration=(hour*60)+minute+duration
print("finishing time:",end="")
print(duration//60,duration/60,sep=":")
