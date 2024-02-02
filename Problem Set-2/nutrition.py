def main():
    # Dictionary mapping fruits to their calories
    fruit_calories = {
        'Apple': 95,
        'Banana': 105,
        'Orange': 62,
        'Strawberries': 4,
        # Add other fruits and their respective calories
    }

    # Prompt user for input
    fruit_input = input("Enter a fruit: ")

    # Convert input to title case for case-insensitivity
    fruit_input = fruit_input.title()

    # Check if the input is a valid fruit in the dictionary
    if fruit_input in fruit_calories:
        calories = fruit_calories[fruit_input]
        print(f"{fruit_input} has {calories} calories per portion.")
    else:
        print("Invalid input. Please enter a valid fruit.")

if __name__ == "__main__":
    main()
