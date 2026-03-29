def find_largest(num1, num2):
    if num1 > num2:
        return f"{num1} is larger"
    elif num2 > num1:
        return f"{num2} is larger"
    else:
        return "Both numbers are equal"


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print(find_largest(first, second))