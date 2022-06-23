year=int(input("enter the year:-"))
month=int(input("enter the month"))
if year%4==0:
    if month==2:
        print("29 days")
    elif month in("1","3","5","7","8"):
        print("31 days")
    else:
        print("30 days")    
    
else:
    if month==2:
        print("28 days")
    elif month in(1,3,5,7,8):
        print("31 days")
    else:
        print("30 days")   