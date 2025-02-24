
import os

loop = True

while loop:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    output = ""


    print("A: Addition")
    print("S: Subtraction")
    print("M: Multiplication")
    print("D: Division")
    choice = input("Which operation you want to perform? ")

    if choice == "A" or choice == 'a':
        output=num1 + num2
        print("Result:", output)
        loop = False
    elif choice == "S" or choice == 's':
        output=num1 - num2
        print("Result:", output)
        loop = False
    elif choice == "M" or choice == 'm':
        output=num1 * num2
        print("Result:", output)
        loop = False
    elif choice == "D" or choice == 'd':
        output=num1 / num2
        print(f"Result: {output:,.2f}")
        loop = False
    else:
        os.system('clear')
        print("Wrong Input!")
        input("Press Any Key to rerun the program\n")
        os.system('clear')
        loop = True



