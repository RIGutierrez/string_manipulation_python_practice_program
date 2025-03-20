while True:
    try:
        # ask user to input numbers
        user_input = int(input("Please input a number (0-1000): "))
        
        # check if number is 0-1000 range
        if 0 <= user_input <= 1000:
            break
        else:
            print("Input must be from 0-1000")
    
    except ValueError:
        print("Please input valid number")

# add zero at the beginning
print(str(user_input).zfill(6))