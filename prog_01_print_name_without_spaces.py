while True:
    # ask user to input their name
    name = input("Please input your fullname (with spaces at the beginning): ")

    # check input if have spaces and not just space
    if name.startswith(" ") and name.strip():
        break

    print("Your input must contain space characters at the beginning")
  
# print without spaces
print(name.strip())