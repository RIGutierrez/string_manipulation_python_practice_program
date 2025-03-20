while True:
    # ask user for input
    input_statement = input("Statement: ").strip()
    
    # check input if invalid
    if not input_statement:
        print("Invalid input. Try again.")
        continue

    break

# print number of words
print(len(input_statement.split()))