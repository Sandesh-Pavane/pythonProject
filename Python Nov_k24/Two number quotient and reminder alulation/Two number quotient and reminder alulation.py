#Math Calculator
num1 = float(input("Enter 1st number : "))
num2 = float(input("Enter 2nd number : "))

choice = int (input("Enter Which opration you want to perform : For  reminder press 1/ For quotient press 2  :  "))
if (choice==1):
    reminder = num1/num2
    print("Result =", reminder)

elif (choice==2):
    quotient = num1 % num2
    print("Result =", quotient)


else:
   print("Invalid choice please select right option")

