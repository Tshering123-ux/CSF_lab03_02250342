# List of numbers
numbers = [2, 4, 6, 8, 10]

# Input the number to search
search_num = int(input("Searching for: "))

# Search using a loop
for num in numbers:
    if num == search_num:
        print("Number found")
        break