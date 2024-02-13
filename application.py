# Importing necessary libraries
from forex_python.converter import CurrencyRates

# Function to fetch real-time exchange rates
def get_exchange_rate(source_currency, target_currency):
    # Initialize CurrencyRates object
    c = CurrencyRates()

    try:
        # Fetch exchange rate
        exchange_rate = c.get_rate(source_currency, target_currency)
        return exchange_rate
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to convert currency
def convert_currency():
    print("Welcome to CurrencyConvertX!")
    
    # Get source and target currencies
    source_currency = input("Enter the source currency code (e.g., USD): ").upper()
    target_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    # Get amount to convert
    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    # Fetch exchange rate
    exchange_rate = get_exchange_rate(source_currency, target_currency)

    if exchange_rate is not None:
        # Convert currency
        converted_amount = round(amount * exchange_rate, 2)
        print(f"{amount} {source_currency} equals {converted_amount} {target_currency}")
    else:
        print("Currency conversion failed. Please try again.")

# Main function
def main():
    while True:
        convert_currency()
        choice = input("Do you want to convert another currency? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using CurrencyConvertX!")
            break

if __name__ == "__main__":
    main()
