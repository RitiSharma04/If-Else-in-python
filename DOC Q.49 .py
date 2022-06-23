year=int(input("enter the year:-"))
month=int(input("enter the month:-"))
day=int(input("enter the day:-"))
if year>0:
    if month<=12:
       if month<=31:
          print(year,'/',month,'/',day+1)  
else:
    print("no")              

