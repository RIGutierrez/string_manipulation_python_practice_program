while True:
    # ask user to input their full name
    name = input("Please input your full name in incorrect casing: ").strip()
    
    # check input if invalid
    if not name:
        print("Invalid input. Try again.")
        continue

    break

# print in reverse casing
print(name.swapcase())