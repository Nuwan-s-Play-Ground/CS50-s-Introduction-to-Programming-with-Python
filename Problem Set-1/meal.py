def main():
    # Prompt the user for a time
    user_time = input("Enter the time in 24-hour format (HH:MM): ")

    # Convert the user input to hours using the convert function
    hours = convert(user_time)

    # Check the time and output the corresponding meal information
    if 7.0 <= hours <= 8.0:
        print("It's breakfast time!")
    elif 12.0 <= hours <= 13.0:
        print("It's lunch time!")
    elif 18.0 <= hours <= 19.0:
        print("It's dinner time!")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(":"))

    # Calculate the total hours, considering there are 60 minutes in 1 hour
    total_hours = hours + (minutes / 60)
    
    return total_hours

if __name__ == "__main__":
    main()
