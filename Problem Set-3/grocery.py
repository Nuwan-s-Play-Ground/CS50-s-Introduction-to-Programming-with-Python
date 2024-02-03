grocery_list = {}

try:
    while True:
        item = input("Enter a grocery item (Ctrl-D to finish): ").title()
        
        # Check if the item is in the grocery list
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

except EOFError:
    # Display the sorted and formatted grocery list
    sorted_items = sorted(grocery_list.items(), key=lambda x: x[0])
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")
