
from utils import load_json, save_json, header, continue_prompt, add_transaction_log
from validation import validation_float
from currency_rates import NAME_CURRENCY, RATES

def withdraw_money():
    header("Výběr peněz z pokladny")
    
    for key, value in NAME_CURRENCY.items():
        print(f"{key} - {value}")
    
    currency_input = input("Vyber číslo měny výběru: ")
    
    if currency_input not in NAME_CURRENCY:
        print(" Neplatný výběr měny.")
        return
    
    currency_code = NAME_CURRENCY[currency_input]
    file_path = "cash_register.json"
    register_data = load_json(file_path)
    
    # We find the balance right at the beginning
    current_balance = register_data.get(currency_code, 0.0)

    # The user will immediately see how much they can withdraw
    print(f"\nAktuální zůstatek v pokladně: {current_balance:.2f} {currency_code}")
    
    if current_balance <= 0:
        print(f" V pokladně není žádná hotovost v měně {currency_code}.")
        return

    amount = validation_float(f"Zadej částku k výběru (max {current_balance:.2f}) nebo dej 'q' pro zrušení: ")
    
    if amount is None or amount <= 0:
        print(" Neplatná částka.")
        return

    # Checking your balance
    if amount > current_balance:
        # If you enter 1500 and there is 500 in the cash register
        print(f"\n CHYBA: Nelze vybrat {amount:.2f} {currency_code}!")
        print(f"V pokladně chybí {(amount - current_balance):.2f} {currency_code}.")
        print("Transační limit překročen. Transakce nebyla uspěšná.")
        continue_prompt()
        return

    # Subtract and save
    register_data[currency_code] -= amount
    save_json(file_path, register_data)
    
    print(f"Úspěšně vybráno {amount} {currency_code}. Transakce byla úspěšná.")
    add_transaction_log("Výběr z pokladny", amount, currency_code, register_data[currency_code])
    print(f"Nový zůstatek {currency_code}: {register_data[currency_code]:.2f}")
    continue_prompt()