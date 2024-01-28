def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    converted_text = text.replace(':)', '🙂').replace(':(', '🙁')
    return converted_text

def main():
    # Prompt the user for input
    user_input = input("Enter text: ")

    # Convert emoticons to emoji
    converted_text = convert(user_input)

    # Print the result
    print("Converted text:", converted_text)

if __name__ == "__main__":
    main()
