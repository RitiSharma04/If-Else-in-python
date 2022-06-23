quantity=int(input("enter the quantity"))
discount=1
cost=0
price=0
if quantity>=1000:
    cost=quantity*10
    discount=cost*10/100
    price=price+cost-discount
else:
    cost=quantity*10 
    price=price+cost   
print("Price","=",price)    