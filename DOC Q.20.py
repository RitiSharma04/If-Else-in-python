electricity_unit=int(input("enter the electricity unit"))
charge=0
if electricity_unit<=50:
    charge=charge+electricity_unit*0.50
elif electricity_unit<=150:
    charge=charge+(electricity_unit-100)*0.50 +(electricity_unit-50)*0.75
elif electricity_unit<=250:
    charge=charge+(electricity_unit-200)*0.50 +(electricity_unit-150)*0.75+(electricity_unit-150) *1.20
elif electricity_unit>250:
    charge=charge+50*0.50+100*0.75+100*1.20+(electricity_unit-250)*1.75
print(charge+electricity_unit*20/100)         
