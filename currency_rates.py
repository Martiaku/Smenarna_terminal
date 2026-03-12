from utils import load_json, save_json

CURRENCY_FILE = "currency_rates.json"


def load_currency_data():
    data = load_json(CURRENCY_FILE)
    if not isinstance(data, dict):
        return {}
    return data


def get_currency_maps():
    data = load_currency_data()
    name_currency = {}
    buy_rates = {}
    sell_rates = {}
    for key, value in data.items():
        if not isinstance(value, dict):
            continue
        name = value.get("name")
        buy = value.get("buy")
        sell = value.get("sell")
        if name is None or buy is None or sell is None:
            continue
        name_currency[str(key)] = str(name)
        try:
            buy_rates[str(key)] = float(buy)
            sell_rates[str(key)] = float(sell)
        except (TypeError, ValueError):
            continue
    return name_currency, buy_rates, sell_rates


def save_currency_data(data):
    save_json(CURRENCY_FILE, data)
