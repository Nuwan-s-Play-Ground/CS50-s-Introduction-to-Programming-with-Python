def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in text:
        if char not in vowels:
            result += char

    return result

def main():
    user_input = input("Enter a text: ")
    result = remove_vowels(user_input)
    
    print("Text without vowels:", result)

if __name__ == "__main__":
    main()
