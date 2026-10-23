STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 170.00,
}


def main():
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(STOCK_PRICES))

    portfolio = {}

    while True:
        symbol = input("Enter a stock symbol (or 'done' to finish): " ).strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("That symbol is not in the price list. Please try again.")
            continue

        try:
            quantity = int(input(f"How many shares of {symbol}? "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a whole number for the quantity.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    if not portfolio:
        print("No stocks were added.")
        return

    total_value = 0.0
    print("\nYour portfolio:")
    for symbol, quantity in portfolio.items():
        value = STOCK_PRICES[symbol] * quantity
        total_value += value
        print(f"{symbol}: {quantity} shares x ${STOCK_PRICES[symbol]:,.2f} = ${value:,.2f}")

    print(f"Total investment value: ${total_value:,.2f}")


if __name__ == "__main__":
    main()
