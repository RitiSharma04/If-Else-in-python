from gettext import find


a=input("enter the string:-")
if "ing"in a:
    a.find("ing")
    print(a+"ly")
else:
    a.find("ly")
    print(a+"ing")    