
from utils import header, continue_prompt
from transfer_money import transfer_money
from next_user import next_user
from change_password import change_password
from cash_register_menu import cash_register_menu
from currency_submenu import currency_menu

# This file contains the main home page of the application.

def home_page():
    while True:
        header("Hlavní menu")
        print("\n1 - Převod peněz\n2 - Určování kurzů\n3 - Pokladna\n4 - Přidání uživatele\n5 - Změna hesla\nq - Ukončení programu")
        choice = input("Vložte prosím číslo požadavku (1-5) nebo 'q' pro ukončení programu: ")
        match choice:
            case "1":
                transfer_money()
            case "2":
                currency_menu()
            case "3":
                cash_register_menu()
            case "4":
                next_user()
            case "5":
                change_password()
            case "q":
                break
            case _:
                print("Tvoje volba není validní, zkus to znovu.")
                continue_prompt()