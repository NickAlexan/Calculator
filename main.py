
def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def star(num1, num2):
    return num1 * num2

def slash(num1, num2):
    return num1 / num2

def count(num1, num2, operation):
    if operation == "+":
        result = plus(num1, num2)
        print(f"{num1} {operation} {num2} = {plus(num1, num2)}")
        return result

    if operation == "-":
        result = minus(num1, num2)
        print(f"{num1} {operation} {num2} = {minus(num1, num2)}")
        return result

    if operation == "*":
        result = star(num1, num2)
        print(f"{num1} {operation} {num2} = {star(num1, num2)}")
        return result

    if operation == "/":
        result = slash(num1, num2)
        print(f"{num1} {operation} {num2} = {slash(num1, num2)}")
        return result


def calculator():
    num1 = float(input("1st number: "))
    go_on = True
    while go_on == True:
        operation = input("Pick an operation:\n+\n-\n*\n/\n")
        num2 = float(input("2nd number: "))
        num1 = count(num1, num2, operation)
        choice = input("Want to continue? y/n? ").lower
        if choice == "n":
            go_on = False

calculator()