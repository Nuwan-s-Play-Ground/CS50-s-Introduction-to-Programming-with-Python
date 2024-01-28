def slow_down_text(input_text):
    # Replace spaces with three periods
    slowed_text = input_text.replace(' ', '...')
    return slowed_text

def main():
    # Prompt the user for input
    user_input = input("Enter text: ")

    # Slow down the text by replacing spaces
    slowed_down_text = slow_down_text(user_input)

    # Output the slowed down text
    print("Slowed down text:", slowed_down_text)

if __name__ == "__main__":
    main()
