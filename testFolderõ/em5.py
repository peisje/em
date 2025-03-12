try:
    num1 = float(input("write first number: "))
    num2 = float(input("write second number: "))
    operator = input("enter operator: ")
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("error: division by zero")
    else:
        result = num1 / num2
 print("Result:", result)