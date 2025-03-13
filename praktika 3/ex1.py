try:
    with open('arvud.txt', 'r') as file:
        lines = file.readlines()  
        
    result = None

    for i in range(0, len(lines), 2):
        numbers = lines[i].split()  
        operation = lines[i + 1].strip()  

        num1 = int(numbers[0])
        num2 = int(numbers[1])

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = num1 / num2
        else:
            print("Error: Unknown operation!")
            continue
        
        print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Division by zero!")
except FileNotFoundError:
    print("Error: File not found!")
except ValueError:
    print("Error: Invalid number format in the file!")
except Exception:
    print("Error: An unexpected error occurred!")
