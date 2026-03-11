
from utils import load_json, save_json, header, continue_prompt
from validation import validation_float

def cashier_balance():
    header("Zůstatek pokladny")
    file_path = "cash_register.json"
    register_data = load_json(file_path)
    if not register_data:
        print("Pokladna je prázdná.")
        continue_prompt()
        return
    print("Aktuální zůstatek v pokladně:")
    for currency, amount in register_data.items():
        print(f"{currency}: {amount:.2f}")
    continue_prompt()
    