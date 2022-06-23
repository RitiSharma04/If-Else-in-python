Month=input("enter the  month:-")
day=int(input("enter the days:-"))
if Month in ("december","januory"):
    if day==31:
        print("this is winter")
elif Month in ("feburary","march"):
    if day==29 or day==28 or day==31:
        print("this is spring")
elif Month in("april","may","june"):
    if day==30 or day ==31:
        print("this is summar")
elif Month in ("july","august","september"):
    if day==31 or day==30:
        print("this is monsoon")
else:
    print("this is autman")                