number_of_unit=int(input("enter the unit"))
amount=0
if number_of_unit<=100:
    print("NO CHARGE")
elif number_of_unit<=200:
    amount=amount+(number_of_unit-100)*5
elif number_of_unit>200:
    amount=amount+100*5 +(number_of_unit-200)*10
print(amount)    
