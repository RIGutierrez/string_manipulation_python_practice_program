while True:
    # ask user to input their full name
    name = input("Please input your full name: ").strip()

    # check input if invalid
    if not name:
        print("Invalid input. Try again.")
        continue

    break

# print number of characters
print(len(name))