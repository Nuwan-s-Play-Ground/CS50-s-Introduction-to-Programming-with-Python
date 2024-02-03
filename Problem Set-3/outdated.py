import re

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

def format_date(month, day, year):
    return f"{year:04d}-{month:02d}-{day:02d}"

def get_date_input():
    while True:
        user_input = input("Enter a date (e.g., 9/8/1636 or September 8, 1636): ").strip()

        # Try to match date in MM/DD/YYYY or Month Day, YYYY formats
        match = re.match(r"(\d{1,2})/(\d{1,2})/(\d{2,4})|(\w+) (\d{1,2}), (\d{2,4})", user_input)

        if match:
            month = months.index(match.group(4).capitalize()) + 1 if match.group(4) else int(match.group(1))
            day = int(match.group(2)) if match.group(2) else int(match.group(5))
            year = int(match.group(3)) if match.group(3) else int(match.group(6))

            return format_date(month, day, year)
        else:
            print("Invalid date format. Please enter a valid date.")

if __name__ == "__main__":
    formatted_date = get_date_input()
    print("Formatted date: ", formatted_date)
