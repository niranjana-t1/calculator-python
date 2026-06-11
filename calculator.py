print("---CALCULATOR---\n")
def add(a,b):
    return f'{a}+{b} is {a+b}'
def sub(a,b):
    return f'{a}-{b} is {a-b}'
def mult(a,b):
    return f'{a}*{b} is {a*b}'
def div(a,b):
    if b==0.0:
        return "Cannot be divided by zero."
    else:
        return f'{a}/{b} is {a/b}'
def power(a,b):
    return f'{a}**{b} is {a**b}'

while True:
    print("--MENU--\n")
    print("+: ADDITION ")
    print("-: SUBTRACTION")
    print("*: MULTIPLICATION")
    print("/: DIVISION")
    print("**: POWER")
    print("Enter exit to exit the calculator")
    operation=input("Enter operation: ")
    if operation == "exit":
        print("Thank you for using the calculator.")
        break
    else:
        if operation not in ["+", "-", "*", "/", "**", "exit"]:
            print("Invalid operation")
            continue
        a=float(input("Enter the first number: "))
        b=float(input("Enter the second number: "))
        if operation == "+":
            print(add(a,b))
        elif operation == "-":
            print(sub(a,b))
        elif operation == "*":
            print(mult(a,b))
        elif operation =="/":
            print(div(a,b))
        elif operation == "**":
            print(power(a,b))
            



