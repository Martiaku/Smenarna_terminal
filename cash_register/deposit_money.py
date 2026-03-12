
from utils import load_json, save_json, header, continue_prompt, add_transaction_log
from validation import validation_float
from currency_rates import get_currency_maps

# Implementation of the function for receiving money into the cash register

def deposit_money():
    header("Příjem peněz do pokladny")
    NAME_CURRENCY, BUY_RATES, SELL_RATES = get_currency_maps()
    
    # Listing me for users
    for key, value in NAME_CURRENCY.items():
        print(f"{key} - {value}")
    
    currency_input = input("Vyber číslo měny vkladu: ")
    
    # 1. NUMBER TO CODE CONVERSION (e.g. "1" -> "CZK")
    # If the user enters "1", we store "CZK" in the JSON
    if currency_input not in NAME_CURRENCY:
        print("Neplatný výběr měny.")
        return
    
    currency_code = NAME_CURRENCY[currency_input] # Here we get "CZK", "EUR", etc.

    file_path = "cash_register.json"
    register_data = load_json(file_path)
    if not register_data:
        register_data = {}

    amount = validation_float(f"Zadej částku v {currency_code}: ")
    
    if amount is None or amount <= 0:
        print("Neplatná částka.")
        return

    # 2. SAVE UNDER CURRENCY CODE (e.g. "CZK": 500.0)
    if currency_code not in register_data:
        register_data[currency_code] = 0.0
    
    register_data[currency_code] += amount
    
    save_json(file_path, register_data)
    
    print(f"Úspěšně vloženo {amount} {currency_code}.")
    add_transaction_log("Příjem do pokladny", amount, currency_code, register_data[currency_code])
    print(f"Nový zůstatek {currency_code}: {register_data[currency_code]:.2f}")
    continue_prompt()
