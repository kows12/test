# Define the function for the calculator
def calc():
    # Get user input for the first number
    num1 = float(input("Enter the first number: "))
    print("enter the valid name")

    # Get user input for the second number
    num2 = float(input("Enter the second number: "))

    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on user input
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation. Please enter a valid operation.")

    # Print the result
    print("The result is: ", result)

# Call the calculator function
calc()
