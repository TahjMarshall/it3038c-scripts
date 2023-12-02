import tkinter as tk
from tkinter import simpledialog, messagebox

def convert_currency(amount, currency, exchange_rates):
    """
    Converts the given amount to the specified currency using the exchange rates.
    """
    if currency in exchange_rates:
        return round(amount * exchange_rates[currency], 2)
    else:
        return None

def get_vacation_spot_currency(vacation_spot, spot_currency_map):
    """
    Returns the currency for the given vacation spot.
    """
    return spot_currency_map.get(vacation_spot, None)

def main():
    # Set up the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Predefined exchange rates and corresponding vacation spots
    exchange_rates = {
        'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0, 'INR': 74.0,
        'CAD': 1.25, 'AUD': 1.30, 'CNY': 6.45, 'BRL': 5.25,
        'RUB': 74.5, 'ZAR': 14.5, 'SGD': 1.35, 'MXN': 20.0
    }
    spot_currency_map = {
        'Paris': 'EUR', 'London': 'GBP', 'Tokyo': 'JPY', 'Delhi': 'INR',
        'Toronto': 'CAD', 'Sydney': 'AUD', 'Beijing': 'CNY', 'Rio': 'BRL',
        'Moscow': 'RUB', 'Cape Town': 'ZAR', 'Singapore': 'SGD', 'Mexico City': 'MXN'
    }
    best_time_to_visit = {
        'Paris': 'Spring (Apr-Jun)', 'London': 'Late Spring (May-Jun)',
        'Tokyo': 'Autumn (Oct-Nov)', 'Delhi': 'Winter (Nov-Mar)',
        'Toronto': 'Summer (Jun-Aug)', 'Sydney': 'Spring (Sep-Nov)',
        'Beijing': 'Autumn (Sep-Nov)', 'Rio': 'Late Spring (Oct-Dec)',
        'Moscow': 'Summer (Jun-Aug)', 'Cape Town': 'Spring (Sep-Nov)',
        'Singapore': 'Winter (Dec-Feb)', 'Mexico City': 'Spring (Apr-May)'
    }

    try:
        # User input for amount and vacation spot
        amount = simpledialog.askfloat("Input", "Enter the amount in USD you plan to spend:", parent=root, minvalue=0)
        if amount is None:
            raise ValueError("No amount entered")

        vacation_spot = simpledialog.askstring("Input", "Enter your vacation spot (e.g., Paris, Tokyo):", parent=root)
        if not vacation_spot:
            raise ValueError("No vacation spot entered")

        # Get currency for the vacation spot and perform conversion
        currency = get_vacation_spot_currency(vacation_spot, spot_currency_map)
        if currency:
            converted_amount = convert_currency(amount, currency, exchange_rates)
            result_message = f"In {vacation_spot}, {amount} USD will be approximately {converted_amount} {currency}."
            messagebox.showinfo("Conversion Result", result_message, parent=root)
        else:
            messagebox.showinfo("Info", "Currency information for this vacation spot is not available.", parent=root)

        # Recommend top 5 locations based on best and worst purchasing power
        converted_amounts = {spot: convert_currency(amount, spot_currency_map[spot], exchange_rates) for spot in spot_currency_map}
        best_spots = sorted(converted_amounts, key=converted_amounts.get, reverse=True)[:5]
        worst_spots = sorted(converted_amounts, key=converted_amounts.get)[:5]

        best_message = "\nTop 5 vacation spots with the best purchasing power for USD:\n"
        for spot in best_spots:
            best_time = best_time_to_visit.get(spot, "Anytime")
            best_message += f"- {spot} ({converted_amounts[spot]} {spot_currency_map[spot]}), Best time to visit: {best_time}\n"

        messagebox.showinfo("Best Spots for Purchasing Power", best_message, parent=root)

        worst_message = "\nTop 5 vacation spots with the worst purchasing power for USD:\n"
        for spot in worst_spots:
            worst_message += f"- {spot} ({converted_amounts[spot]} {spot_currency_map[spot]})\n"

        messagebox.showinfo("Worst Spots for Purchasing Power", worst_message, parent=root)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve), parent=root)
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=root)

if __name__ == "__main__":
    main()
