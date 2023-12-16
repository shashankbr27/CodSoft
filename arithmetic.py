number1=float(input("Enter the first no. "))
number2=float(input("Enter the second no. "))
print("Press\n A-Addition\n S-Subtraction\n M-Multiplication\n D-Divison\n ")
choice=input("Enter your choice: ")
if(choice.upper()=="A"):
    print(number1+number2)
elif(choice.upper()=="S"):
    print(number1-number2)
elif(choice.upper()=="M"):
    print(number1*number2)
elif(choice.upper()=="D"):
    if(number2==0):
        print("Can't divide by zero! ")
    else:
        print(number1/number2)
else:
    print("Select the options from above!")