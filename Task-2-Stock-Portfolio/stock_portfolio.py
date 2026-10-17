
# Task 2: Stock Portfolio Tracker
# Datheon Python Programming Internship

import os

# Available stocks and sample prices (in rupees)
STOCKS = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "GOOGL": 150.0,
    "MSFT": 420.0
}

# Dictionary to store stock quantities
portfolio = {}


def display_available_stocks():
    """Display available stocks and their sample prices."""
    print("\nAvailable stocks and sample prices:")
    for ticker, price in STOCKS.items():
        print(f"{ticker} - Rs. {price:.2f}")


def add_stock():
    """Add shares to the portfolio."""
    display_available_stocks()

    ticker = input("\nEnter stock ticker: ").strip().upper()

    if ticker not in STOCKS:
        print("Stock not available. Choose a listed ticker.")
        return

    try:
        quantity = int(input("Enter number of shares: "))

        if quantity <= 0:
            print("Please enter a quantity greater than zero.")
            return

    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        return

    # Add to existing quantity if the stock is already present
    portfolio[ticker] = portfolio.get(ticker, 0) + quantity

    total_shares = portfolio[ticker]
    holding_value = total_shares * STOCKS[ticker]

    print("\nStock added successfully!")
    print(f"Total shares of {ticker}: {total_shares}")
    print(f"Holding value: Rs. {holding_value:.2f}")


def view_portfolio():
    """Display all holdings and total portfolio value."""
    print("\n===== YOUR PORTFOLIO =====")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_value = 0.0

    for ticker, quantity in portfolio.items():
        price = STOCKS[ticker]
        holding_value = quantity * price
        total_value += holding_value

        print(f"\nTicker: {ticker}")
        print(f"Shares: {quantity}")
        print(f"Sample price: Rs. {price:.2f}")
        print(f"Holding value: Rs. {holding_value:.2f}")

    print(f"\nTotal portfolio value: Rs. {total_value:.2f}")


def save_portfolio():
    """Save portfolio details to a text file."""
    filename = "portfolio.txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("STOCK PORTFOLIO TRACKER\n")
            file.write("======================\n\n")

            if not portfolio:
                file.write("Your portfolio is empty.\n")
            else:
                total_value = 0.0

                for ticker, quantity in portfolio.items():
                    price = STOCKS[ticker]
                    holding_value = quantity * price
                    total_value += holding_value

                    file.write(f"Ticker: {ticker}\n")
                    file.write(f"Shares: {quantity}\n")
                    file.write(f"Sample price: Rs. {price:.2f}\n")
                    file.write(
                        f"Holding value: Rs. {holding_value:.2f}\n\n"
                    )

                file.write(
                    f"Total portfolio value: Rs. {total_value:.2f}\n"
                )

        print(f"Portfolio saved successfully to {os.path.abspath(filename)}")

    except OSError as error:
        print(f"Could not save portfolio: {error}")


def main():
    """Run the stock portfolio tracker."""
    print("===== STOCK PORTFOLIO TRACKER =====")

    display_available_stocks()

    while True:
        print("\n1. Add stock")
        print("2. View portfolio")
        print("3. Save portfolio to a text file")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_stock()

        elif choice == "2":
            view_portfolio()

        elif choice == "3":
            save_portfolio()

        elif choice == "4":
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
