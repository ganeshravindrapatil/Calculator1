# Function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation choice."

# Main function to take inputs and display results
def main():
    print("Welcome to the Simple Calculator")
    
    try:
        # Take input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Choose the operation you want to perform:")
        print("Enter '+' for addition")
        print("Enter '-' for subtraction")
        print("Enter '*' for multiplication")
        print("Enter '/' for division")
        
        operation = input("Enter your operation choice: ")
        
        # Perform calculation and display result
        result = calculate(num1, num2, operation)
        print(f"Result: {result}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    main()
