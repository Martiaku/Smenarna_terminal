
from utils import header, continue_prompt
from currency_rates import NAME_CURRENCY, RATES

# This code for the transfer money

def transfer_money():
    while True:
        header("Výpočet směny měn")
        for key, value in NAME_CURRENCY.items():
            print(f"{key} - {value}")   
        currency_input = input("Vlož číslo měny vstupu: ")
        if currency_input == "q":
            break
        
        currency_output = input("Vlož číslo měny výstupu: ")
        if currency_output == "q":
            break
        
        # Check, exist CURRENCY
        if currency_input not in NAME_CURRENCY or currency_output not in NAME_CURRENCY:
            print("Chyba: Neplatný výběr měny")
            continue_prompt()
            continue
        
        try:
            amount = float(input(f"Zadej částku v {NAME_CURRENCY[currency_input]}: "))
        except ValueError:
            print("Chyba: Musíš zadat číslo (např. 100.50)!")
            continue_prompt()
            continue
        
        v_korunach = amount * RATES[currency_input]
        vysledek = v_korunach / RATES[currency_output]

        print(f"\nHOTOVO: {amount} {NAME_CURRENCY[currency_input]} = {vysledek:.2f} {NAME_CURRENCY[currency_output]}")
        continue_prompt()
        break