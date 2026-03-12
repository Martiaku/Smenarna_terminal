
from utils import load_json, save_json, header, continue_prompt
from validation import validation_float

def transaction_history():
    header("Historie transakcí")
    logs = load_json("cash_register_transactions.json")
    
    if not logs:
        print("Žádné transakce nebyly nalezeny.")
    else:
        print(f"{'Čas':<20} | {'Typ':<20} | {'Částka':<20} | {'Měna':<8} | {'Uživatel':<12}")
        print("-" * 65)
        for log in logs:
            t_type = log['type']
            print(f"{log['ts']:<20} | {t_type:<20} | {log['amount']:<20.2f} | {log['currency']:<8} | {log['user']:<12}")
    
    continue_prompt()