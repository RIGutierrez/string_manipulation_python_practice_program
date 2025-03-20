while True:
    # ask user to input their full name
    name = input("Please input your full name in incorrect casing: ")
    
    # check input if invalid
    if not name:
        print("Invalid input. Try again.")
        continue

    # convert to snake case
    name_snake = name.strip().lower().replace(" ", "_")
    break

# print in snake case
print(name_snake)