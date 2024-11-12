#Math Calculator
num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))

choice = int (input("Enter Which opration you want to perform : For Add press 1/ For Substraction press 2 /For multipiation press 3/for devition press 4  :  "))
if (choice==1):
    result = num1+num2
elif (choice==2):
    result = num1 - num2

elif (choice == 3):
    result = num1  * num2

elif (choice == 4):
    result = num1 / num2

else:
   print("Invalid choice please select right option")

print("Result =", result)