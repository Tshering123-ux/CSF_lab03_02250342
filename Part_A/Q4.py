def find_largest(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return f"{num1} is the largest number"
        else:
            return f"{num3} is the largest number"
    else:
        if num2 >= num3:
            return f"{num2} is the largest number"
        else:
            return f"{num3} is the largest number"

a, b, c = map(int, input("Enter three numbers: ").split())
print(find_largest(a, b, c))