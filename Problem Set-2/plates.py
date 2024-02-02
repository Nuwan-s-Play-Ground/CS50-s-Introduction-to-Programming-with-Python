def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the plate has the correct length
    if not has_correct_length(s):
        return False

    # Check if the plate has the correct format
    if not has_correct_format(s):
        return False

    # Check if the plate has valid characters
    if not has_valid_characters(s):
        return False

    # Check additional requirements as needed

    # If all checks pass, the plate is valid
    return True

def has_correct_length(s):
    return len(s) == 7

def has_correct_format(s):
    return s[0:3].isalpha() and s[3:7].isdigit()

def has_valid_characters(s):
    valid_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return all(char in valid_characters for char in s)

if __name__ == "__main__":
    main()
