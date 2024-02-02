def calculate_percentage(fraction):
    try:
        # Split the input fraction into X and Y
        x, y = map(int, fraction.split('/'))

        # Check if Y is not 0 and X is less than or equal to Y
        if y != 0 and x <= y:
            percentage = (x / y) * 100

            # Check the percentage and output accordingly
            if percentage <= 1:
                result = "E"
            elif percentage >= 99:
                result = "F"
            else:
                result = round(percentage)

            return result
        else:
            return None

    except (ValueError, ZeroDivisionError):
        return None

def main():
    while True:
        fraction_input = input("Enter the fuel fraction (X/Y): ")

        percentage = calculate_percentage(fraction_input)

        if percentage is not None:
            print(f"The tank is {percentage}% full.")
            break
        else:
            print("Invalid input. Please enter a valid fraction.")

if __name__ == "__main__":
    main()
