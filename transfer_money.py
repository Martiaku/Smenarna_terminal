
from utils import header, continue_prompt
from currency_rates import NAME_CURRENCY, RATES

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
        
        # Input validation: ensure the user enters a valid numeric amount
        try:
            amount = float(input(f"Zadej částku v {NAME_CURRENCY[currency_input]}: "))
        except ValueError:
            print("Chyba: Musíš zadat číslo (např. 100.50)!")
            continue_prompt()
            continue
        
        v_korunach = amount * RATES[currency_input]
        vysledek = v_korunach / RATES[currency_output]

        print(f"\nPřevod: {amount} {NAME_CURRENCY[currency_input]} = {vysledek:.2f} {NAME_CURRENCY[currency_output]} při kurzu {RATES[currency_output]:.2f} Kč/{NAME_CURRENCY[currency_output]}")
        continue_prompt()
        break