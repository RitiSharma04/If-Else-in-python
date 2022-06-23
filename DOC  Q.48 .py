num1=int(input("enter the num1:-"))
num2=int(input("enter the num2:-"))
num3=int(input("enter the num3:-"))
if num1>num2>num3 or num3>num2>num1:
    print(num2,"is median")
elif num2>num1>num3 or num3>num1>num2:
    print(num1,"is median")
else:
    print(num3,"is median")    
