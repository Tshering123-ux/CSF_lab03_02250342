def add_numbers(a, b):
    return a + b

# Input two numbers
x, y = map(int, input("Enter two numbers: ").split())
print("Sum =", add_numbers(x, y))