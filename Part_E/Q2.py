def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("Enter choice: "))
    
    if choice == 5:
        print("Exiting...")
        break
    
    num1, num2 = map(float, input("Enter two numbers: ").split())
    
    if choice == 1:
        print("Sum =", add(num1, num2))
    elif choice == 2:
        print("Difference =", subtract(num1, num2))
    elif choice == 3:
        print("Product =", multiply(num1, num2))
    elif choice == 4:
        print("Quotient =", divide(num1, num2))
    else:
        print("Invalid choice")