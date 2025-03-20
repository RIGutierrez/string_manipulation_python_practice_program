while True:
    # ask user to input their fullname
    name = input("Please input your fullname: ").strip()

    # check input if invalid
    if not name:
        print("Invalid input. Try again.")
        continue

    break

# print number of characters
print(len(name))