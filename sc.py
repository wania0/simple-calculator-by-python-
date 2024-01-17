no_1= int(input("Enter first number: "))
print("press +,-,/,*")
operator= input("Enter an operator: ")
no_2=int(input("Enter second number: "))
if operator =="+":
    print("first number + second number = ",no_1 + no_2)
elif operator =="-":
    print("first number - second number = ",no_1-no_2)
elif operator =="*":
    print("first number * second number = ",no_1 * no_2)
elif operator =="/":
    print ("first number / second number = ",no_1 / no_2)
else:
    print("invalid input")
         
