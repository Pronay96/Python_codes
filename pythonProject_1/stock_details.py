def check_availability(item, quantity, stock):
    for key, value in stock.items():
        if key == item and value > 0 and value >= quantity:
            return True
        if key == item and value == 0 or value < quantity:
            return False


def place_order(item, quantity, stock, prices):
    total_amount = 0
    for key, value in stock.items():
        if key == item:
            stock[key] = value - quantity
    for key, value in prices.items():
        if key == item:
            total_amount = quantity * value
    print(f"Total amount: {total_amount}")
    print("Remaining stock details")
    for key, value in stock.items():
        print(f"{key}: {value}")


def main():
    stock = {"Sports Balls": 56, "Shin Guard": 50, "Gloves": 60, "Footwear": 15}
    price = {"Sports Balls": 499, "Shin Guard": 249, "Gloves": 369, "Footwear": 999}
    print(stock)
    print(price)
    item_name = input("Enter an item: ")
    quantity = int(input("Enter a quantity: "))
    check = check_availability(item_name, quantity, stock)
    if check:
        place_order(item_name, quantity, stock, price)
    else:
        print("Item is not available")


main()
