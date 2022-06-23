from numpy import safe_eval


year_of_service=int(input("enter the year"))
salery=int(input("enter the salery"))
bonus=0
if year_of_service>5:
    bonus=bonus+salery*5/100
else:
    bonus=0
print("bonus","=",bonus)        

