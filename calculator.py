# Calculater

first = float(input("Enter the first number:"))
second = float(input("Enter the second number:"))
operator = input("Please input the operator:")
if operator == '+':
    print("Answer =",(first+second))
elif operator == '-':
    print("Answer =",(first-second))
elif operator == '*':
    print("Answer =",(first*second))
elif operator == '%':
    print("Answer =",(first%second))
elif operator == '**':
    print("Answer =",(first**second))
elif operator == '/':
    print("Answer =",(first/second))
else:
    print("You Entered An Invalid Operator Please Check It And Try Again.")





