def deep_thought():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    
    # Convert the user input to lowercase for case-insensitive comparison
    user_input_lower = user_input.lower()

    # Check if the user input is equal to any of the accepted answers
    if user_input_lower == "42" or "forty-two" in user_input_lower or "forty two" in user_input_lower:
        print("Yes")
    else:
        print("No")

# Call the function to run the program
deep_thought()
