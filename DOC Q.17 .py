sale_price=int(input("enter the sale price:-"))
cost_price=int(input("enter the num:-"))
quantity=int(input("enter the quantity"))
profit=0
loss=0
if cost_price*quantity>sale_price*quantity:
    loss=loss+(cost_price*quantity)-(sale_price*quantity)
    print("loss:-",loss)
    
elif (cost_price*quantity)==(sale_price*quantity):
    print("no change")  
else:
    profit=profit+(sale_price*quantity)-(cost_price*quantity)  
    print("profit:-",profit)

