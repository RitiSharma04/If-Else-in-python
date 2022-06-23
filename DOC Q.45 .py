number_of_days=int(input("enter the num:-"))
charge=0
if number_of_days<=5:
    charge=charge+2
elif number_of_days>=6 and number_of_days<10:
    charge=charge+3  
elif number_of_days>=10 and number_of_days<15:
    charge=charge+4
elif number_of_days>=15:
    charge=charge+5
print(charge)        