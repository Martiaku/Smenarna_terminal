
from utils import header, continue_prompt, load_json, save_json, add_transaction_log
from currency_rates import NAME_CURRENCY, RATES
from validation import validation_float

# Main function for currency conversion logic

def transfer_money():
    while True:
        header("Výpočet směny měn")
        # Display available currencies dynamically from the rates file
        for key, value in NAME_CURRENCY.items():
            print(f"{key} - {value}")
            
        # Get input currency selection
        currency_input = input("Vlož číslo měny vstupu: ")
        if currency_input == "q":
            break
        
        # Get output currency selection
        currency_output = input("Vlož číslo měny výstupu: ")
        if currency_output == "q":
            break
        
        # Membership test: check if the selected keys exist in our datebase
        if currency_input not in NAME_CURRENCY or currency_output not in NAME_CURRENCY:
            print("Chyba: Neplatný výběr měny")
            continue_prompt()
            return
        
        amount = validation_float("Zadejte částku, kterou chcete převést: ")
        if amount is None:
            break
        # 1. Calculation of the result
        in_CZK = amount * RATES[currency_input]
        result = in_CZK / RATES[currency_output]
        
        # 2. CHECK: Do we have enough currency in the cash register to dispense?
        file_path = "cash_register.json"
        register_data = load_json(file_path)
        if not register_data:
            register_data = {}
        balance_output_currency = register_data.get(NAME_CURRENCY[currency_output], 0.0)
        
        if result > balance_output_currency:
            print(f"CHYBA: Nedostatek {NAME_CURRENCY[currency_output]} v pokladně!")
            continue_prompt()
            return
        
        # 3. MAKING A CHANGE IN A FILE
        register_data[NAME_CURRENCY[currency_input]] = register_data.get(NAME_CURRENCY[currency_input], 0.0) + amount
        register_data[NAME_CURRENCY[currency_output]] = register_data.get(NAME_CURRENCY[currency_output], 0.0) - result
        save_json(file_path, register_data)
        
        # 4. LOGGING THE TRANSACTION
        add_transaction_log("Příjem z převodu", amount, NAME_CURRENCY[currency_input], register_data[NAME_CURRENCY[currency_input]])
        add_transaction_log("Výdej z převodu", result, NAME_CURRENCY[currency_output], register_data[NAME_CURRENCY[currency_output]])

        print("Převod úspěšný!")
        print(f"\nPřevod: {amount} {NAME_CURRENCY[currency_input]} = {result:.2f} {NAME_CURRENCY[currency_output]} při kurzu {RATES[currency_output]:.2f} Kč/{NAME_CURRENCY[currency_output]}")
        continue_prompt()