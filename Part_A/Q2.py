def check_even_odd(num):
    if num % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"


number = int(input("Enter a number: "))
print(check_even_odd(number))