def interpreter_program():
    # Prompt the user for an arithmetic expression
    user_input = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    # Split the expression into components: x, operator, z
    components = user_input.split()

    # Check if there are exactly 3 components (x, operator, z)
    if len(components) != 3:
        print("Invalid input. Please provide an expression in the format 'x y z'.")
        return

    x, operator, z = components

    try:
        # Convert x and z to integers
        x = int(x)
        z = int(z)

        # Perform the calculation based on the operator
        result = 0.0
        if operator == '+':
            result = x + z
        elif operator == '-':
            result = x - z
        elif operator == '*':
            result = x * z
        elif operator == '/':
            # Assuming z is not 0 (as per the hint)
            result = x / z

        # Output the result formatted to one decimal place
        print(f"The result is: {result:.1f}")

    except ValueError:
        print("Invalid input. Please provide valid integers for x and z.")
        return

# Call the function to run the program
interpreter_program()
