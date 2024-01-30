def bank_program():
    user_greeting = input("Please enter your greeting: ")

    # Remove leading whitespace and convert the greeting to lowercase for case-insensitive comparison
    user_greeting = user_greeting.lstrip().lower()

    # Check the conditions and output the corresponding amount
    if user_greeting.startswith("hello"):
        print("$0")
    elif user_greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

# Call the function to run the program
bank_program()
