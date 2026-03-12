from utils import header, continue_prompt, add_transaction_log
from currency_rates import get_currency_maps, load_currency_data, save_currency_data
from validation import validation_float


def rate_adjustment():
    while True:
        header("Úprava kurzů měn")

        NAME_CURRENCY, BUY_RATES, SELL_RATES = get_currency_maps()
        for key, value in NAME_CURRENCY.items():
            current_buy = BUY_RATES.get(key, "N/A")
            current_sell = SELL_RATES.get(key, "N/A")
            print(f"{key} - {value} (Nákup: {current_buy} Kč, Prodej: {current_sell} Kč)")

        currency_choice = input("\nVlož číslo měny (nebo 'q' pro návrat): ")
        if currency_choice == "q":
            break

        if currency_choice not in NAME_CURRENCY:
            print("Chyba: Neplatný výběr měny")
            continue_prompt()
            continue

        rate_type = input("Upravujete nákup (b) nebo prodej (s)? ").strip().lower()
        if rate_type not in ("b", "s"):
            print("Chyba: Zadejte 'b' pro nákup nebo 's' pro prodej.")
            continue_prompt()
            continue

        new_rate = validation_float(
            f"Zadejte nový kurz pro {NAME_CURRENCY[currency_choice]} (v Kč): "
        )
        if new_rate is None:
            break

        data = load_currency_data()
        if currency_choice not in data or not isinstance(data[currency_choice], dict):
            data[currency_choice] = {"name": NAME_CURRENCY[currency_choice], "buy": None, "sell": None}

        if rate_type == "b":
            old_rate = BUY_RATES.get(currency_choice)
            data[currency_choice]["buy"] = new_rate
            rate_label = "Nákup"
        else:
            old_rate = SELL_RATES.get(currency_choice)
            data[currency_choice]["sell"] = new_rate
            rate_label = "Prodej"

        save_currency_data(data)

        add_transaction_log(
            t_type="Změna kurzu",
            amount=new_rate,
            currency=f"{NAME_CURRENCY[currency_choice]} ({rate_label})",
            balance_after=old_rate,
        )

        print(
            f"\nÚspěšně změněno. {NAME_CURRENCY[currency_choice]} {rate_label}: {old_rate} -> {new_rate} Kč."
        )
        continue_prompt()
