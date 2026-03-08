
from utils import header, continue_prompt
from transfer_money import transfer_money
from next_user import next_user
from change_password import change_password

# This file contains the main home page of the application.

def home_page():
    while True:
        header("Hlavní menu")
        print("\n1 - Převod peněz\n2 - Určování kurzů\n3 - Pokladna\n4 - Vložení měny\n5 - Nový uživatel\n6 - Změna hesla\nq - Ukončení programu")
        choice = input("Vložte prosím číslo požadavku (1-6) nebo 'q' pro ukončení programu: ")
        match choice:
            case "1":
                print("Zde bude impretace pro výpočet převodu")
                print("Táto funkce bude v budoucí aktualizaci aplikována.")
                continue_prompt()
                transfer_money()
            case "2":
                print("Zde bude impretace pro určení kurzů měn")
                print("Táto funkce bude v budoucí aktualizaci aplikována.")
                continue_prompt()
            case "3":
                print("Zde bude impretace pro pokladnu")
                print("Táto funkce bude v budoucí aktualizaci aplikována.")
                continue_prompt()
            case "4":
                print("Zde bude impretace pro vložení měn")
                print("Táto funkce bude v budoucí aktualizaci aplikována.")
                continue_prompt()
            case "5":
                next_user()
            case "6":
                change_password()
            case "q":
                break
            case _:
                print("Tvoje volba není validní, zkus to znovu.")
                continue_prompt()