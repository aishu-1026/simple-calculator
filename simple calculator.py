num1=int(input('enter a number1'))
num2=int(input('enter a number2'))
operator=input("enter operator")

if operator == '+':
    print("addition",num1+num2)
elif operator == '-':
    print("subtraction",num1-num2)
elif operator == '*':
    print("multipcation",num1*num2)
elif operator == '/': 
    print("division",num1/num2)
else:
    print("invalid") 