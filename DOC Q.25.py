Number_of_classes_held=int(input("enter the Number of classes held"))
Number_of_classes_attended=int(input("enter the Number of classes attended"))
percentage=Number_of_classes_held/Number_of_classes_attended*100
if percentage>70:
    print("she is able to give exam")
else:
    print("she is no able to give exam")
        
