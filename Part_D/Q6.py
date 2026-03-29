def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Input from user
n = int(input("Enter number: "))
multiplication_table(n)