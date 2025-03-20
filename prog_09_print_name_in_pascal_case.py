while True:
    # ask user to input their full name 
    name = input("Please input your fullname in incorrect casing: ")

    # check input if invalid
    if not name:
        print("Invalid input. Try again.")
        continue

    
    name_pascal = name.strip().title().replace(" ", "")
    break

# print in pascal case
print(name_pascal)