cost_price=int(input("enter the cost price"))
rode_tax=0
if cost_price>100000:
    rode_tax=rode_tax+cost_price*15/100
elif cost_price>50000 and cost_price<=100000:
    rode_tax=rode_tax+cost_price*10/100
elif cost_price<=50000:
    rode_tax=rode_tax+cost_price*5/100
print(rode_tax)        
