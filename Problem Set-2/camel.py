def camel_to_snake(camel_case):
    snake_case = ""

    # Iterate through each character in the camel case string
    for char in camel_case:
        # Check if the character is uppercase
        if char.isupper():
            # Convert uppercase character to lowercase and add an underscore before it
            snake_case += "_" + char.lower()
        else:
            # Keep the lowercase characters unchanged
            snake_case += char

    # Remove the leading underscore if it exists
    snake_case = snake_case.lstrip('_')

    return snake_case

def main():
    # Prompt the user for a variable name in camel case
    camel_case_input = input("Enter a variable name in camel case: ")

    # Convert the camel case to snake case using the function
    snake_case_output = camel_to_snake(camel_case_input)

    # Output the result
    print(f"The variable name in snake case is: {snake_case_output}")

if __name__ == "__main__":
    main()
