from utils import header
from currency_menu.rate_adjustement import rate_adjustment
from currency_menu.rate_change_history import rate_change_history
# 

def currency_menu():
    while True:
        header("Správa měn-MENU")
        print("1 - Upravit kurz měny")
        print("2 - Přidat novou měnu")
        print("3 - Smazat měnu")
        print("4 - Historie změn kurzů")
        print("q - Návrat do hlavního menu")
        choice = input("Vložte prosím číslo požadavku (1-4) nebo 'q' pro návrat do hlavního menu: ")
        match choice:
            case "1":
                rate_adjustment()
            case "2":
                pass
            case "3":
                pass
            case "4":
                rate_change_history()
            case "q":
                break
            case _:
                print("Neplatná volba. Zadejte prosím číslo požadavku (1-4) nebo 'q' pro návrat do hlavního menu.")
                