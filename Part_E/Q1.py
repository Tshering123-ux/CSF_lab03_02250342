def even_odd_upto(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} -> Even")
        else:
            print(f"{i} -> Odd")

# Input from user
n = int(input("Enter n: "))
even_odd_upto(n)