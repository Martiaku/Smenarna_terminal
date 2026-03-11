
from utils import header, continue_prompt
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
            continue
        
        amount = validation_float("Zadejte částku, kterou chcete převést: ")
        if amount is None:
            break
        in_CZK = amount * RATES[currency_input]
        result = in_CZK / RATES[currency_output]

        print(f"\nPřevod: {amount} {NAME_CURRENCY[currency_input]} = {result:.2f} {NAME_CURRENCY[currency_output]} při kurzu {RATES[currency_output]:.2f} Kč/{NAME_CURRENCY[currency_output]}")
        continue_prompt()
        break