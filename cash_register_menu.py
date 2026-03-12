from utils import header
from cash_register.deposit_money import deposit_money
from cash_register.withdraw_money import withdraw_money
from cash_register.cashier_balance import cashier_balance
from cash_register.transaction_history import transaction_history


# 

def cash_register_menu():
    while True:
        header("Pokladna-MENU")
        print("1 - Příjem peněz do pokladny")
        print("2 - Výdej peněz z pokladny")
        print("3 - Stav pokladny")
        print("4 - Historie transakcí")
        print("q - Návrat do hlavního menu")
        choice = input("Vložte prosím číslo požadavku (1-4) nebo 'q' pro návrat do hlavního menu: ")
        match choice:
            case "1":
                deposit_money()
            case "2":
                withdraw_money()
            case "3":
                cashier_balance()
            case "4":
                transaction_history()
            case "q":
                break
            case _:
                print("Neplatná volba. Zadejte prosím číslo požadavku (1-4) nebo 'q' pro návrat do hlavního menu.")
                