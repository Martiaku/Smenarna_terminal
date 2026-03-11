
from utils import load_json, save_json, header, continue_prompt
from validation import validation_float

def transaction_history():
    header("Historie transakcí")
    logs = load_json("cash_register_transactions.json")
    
    if not logs:
        print("Žádné transakce nebyly nalezeny.")
    else:
        print(f"{'Čas':<20} | {'Typ':<10} | {'Částka':<10} | {'Měna':<5} | {'Uživatel':<10}")
        print("-" * 65)
        for log in logs:
            t_type = log['type']
            print(f"{log['ts']:<20} | {t_type:<10} | {log['amount']:<10.2f} | {log['currency']:<5} | {log['user']:<10}")
    
    continue_prompt()