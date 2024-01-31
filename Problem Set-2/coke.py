def main():
    total_amount_due = 50
    current_amount_inserted = 0

    while current_amount_inserted < total_amount_due:
        coin = get_valid_coin_input()
        current_amount_inserted += coin
        remaining_amount_due = total_amount_due - current_amount_inserted

        if remaining_amount_due > 0:
            print(f"Amount due: {remaining_amount_due} cents")
        elif remaining_amount_due == 0:
            print("Amount paid in full. Thank you!")
        else:
            change_due = abs(remaining_amount_due)
            print(f"Amount paid in full. Change due: {change_due} cents")

def get_valid_coin_input():
    valid_coins = [25, 10, 5]

    while True:
        try:
            coin = int(input("Insert a coin (25, 10, or 5 cents): "))
            if coin in valid_coins:
                return coin
            else:
                print("Invalid coin. Please insert a valid coin.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
