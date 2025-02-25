print("Welcome to the Basic Calculator!")

# Get first number with error handling
try:
    num1 = float(input("Enter the first number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Get operator
operator = input("Enter the operation (+, -, *, /): ")

if operator not in ('+', '-', '*', '/'):
    print("Invalid operator! Please use +, -, *, or /.")
    exit()

# Get second number with error handling
try:
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# Perform calculation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2

# Display formatted result
if result == int(result):
    print(f"Result: {int(result)}")
else:
    print(f"Result: {result}")