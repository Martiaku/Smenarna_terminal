from utils import load_json, header, continue_prompt, add_transaction_log


def rate_change_history():
    header("Historie změn kurzů")
    logs = load_json("cash_register_transactions.json")
    
    # We filter out only records of the type "Change in exchange rate"
    rate_logs = [log for log in logs if log.get('type') == "Změna kurzu"]
    
    if not rate_logs:
        print("Žádné změny kurzů nebyly nalezeny.")
    else:
        # In the header, instead of "Amount", write "New rate" and instead of "Balance", write "Old rate"
        print(f"{'Čas':<20} | {'Měna':<8} | {'Nový kurz':<12} | {'Původní':<12} | {'Uživatel':<10}")
        print("-" * 75)
        
        for log in rate_logs:
            # We will take advantage of the fact that you stored the original exchange rate in 'balance_after'
            ts = log.get('ts', 'N/A')
            currency = log.get('currency', '???')
            new_rate = log.get('amount', 0.0)
            old_rate = log.get('balance_after', 0.0)
            user = log.get('user', '???')
            
            print(f"{ts:<20} | {currency:<8} | {new_rate:<12.2f} | {old_rate:<12.2f} | {user:<10}")
    
    print("-" * 75)
    continue_prompt() 