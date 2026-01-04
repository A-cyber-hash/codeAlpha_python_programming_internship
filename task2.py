# TASK 2: Stock Portfolio Tracker

def stock_tracker():
    # Stock prices (hardcoded for simplicity)
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 140.25,
        "MSFT": 350.00,
        "AMZN": 130.80,
        "NVDA": 420.30
    }
    
    portfolio = {}
    
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")
    
    # Get user input for stocks
    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        
        if stock == 'DONE':
            break
            
        if stock not in stock_prices:
            print("Stock not available! Please choose from the list above.")
            continue
            
        try:
            shares = int(input(f"How many shares of {stock}? "))
            if shares <= 0:
                print("Please enter a positive number of shares.")
                continue
                
            # Add to portfolio (or update existing)
            if stock in portfolio:
                portfolio[stock] += shares
            else:
                portfolio[stock] = shares
                
            print(f"Added {shares} shares of {stock}")
            
        except ValueError:
            print("Please enter a valid number!")
    
    # Display portfolio summary
    if not portfolio:
        print("\nNo stocks in portfolio!")
        return
    
    print("\n=== Portfolio Summary ===")
    total_value = 0
    
    for stock, shares in portfolio.items():
        price = stock_prices[stock]
        value = shares * price
        total_value += value
        print(f"{stock}: {shares} shares @ ${price:.2f} = ${value:.2f}")
    
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")
    
    # Ask if user wants to save to file
    save_choice = input("\nSave portfolio to file? (y/n): ").lower()
    if save_choice == 'y':
        filename = "my_portfolio.txt"
        try:
            with open(filename, "w") as file:
                file.write("My Stock Portfolio\n")
                file.write("==================\n\n")
                
                for stock, shares in portfolio.items():
                    price = stock_prices[stock]
                    value = shares * price
                    file.write(f"{stock}: {shares} shares @ ${price:.2f} = ${value:.2f}\n")
                
                file.write(f"\nTotal Value: ${total_value:.2f}\n")
            
            print(f"Portfolio saved to {filename}")
            
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    stock_tracker()