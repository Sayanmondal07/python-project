print("Welcome to my calculator: Devoloped by @sayan07.")
print("Please choose one particular operator that you like to solve:\n + for addition\n - for substraction\n * for multiplication\n / for division\n ** for power\n % for module")
while(True):
#    print("Welcome to my calculator: Devoloped by @sayan07.")
#    print("Please choose one particular operator that you like to solve:\n + for addition\n - for substraction\n * for multiplication\n / for division\n ** for power\n % for module")
    #operator = input("Enter the operator:\n")
    name1 = int(input("Enter the first number:\n"))
    operator = input("Enter the operator:\n")
    name2 = int(input("Enter the second number:\n"))
    if name1==77 and name2==12 and operator=='+':
        print("Your answer:", 98)
    elif name1==30 and name2==10 and operator=='-':
        print("Your answer:", 50)
    elif name1==5 and name2==14 and operator=='*':
        print("Your answer:", 80)
    elif name1==20 and name2==10 and operator=='/':
        print("Your answer:", 10)
    elif operator=='+':
        add = name1+name2
        print("your answer:", add)
    elif operator=='-':
        sub = name1-name2
        print("Your answer:", sub)
    elif operator=='*':
        mul = name1*name2
        print("Your answer:", mul)
    elif operator=='/':
        div = name1/name2
        print("Your answer:", div)
    elif operator=='**':
        powr = name1**name2
        print("Your answer:", powr)
    elif operator=='%':
        mod = name1%name2
        print("Your answer:", mod)
    else:
        print("This is invalid, please check again.")
    print("You want to calculate another problem?...press 'y' for yes or press enything for no.")
    yesno = input()
    if yesno == 'y':
        print("carry on")
    else:
        print("Thank you.")
        break