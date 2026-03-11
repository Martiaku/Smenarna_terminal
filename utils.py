

# This file contains "helper functions"

import os
import json
from datetime import datetime
current_user = "Neznámý uživatel"

def clear_terminal():
    """Clear the console"""
    os.system("cls" if os.name == "nt" else "clear")
    
    
def continue_prompt():
    input("Stiskni Enter pro pokračování...")


def set_current_user(username):
    """Set the current user for personalized greetings"""
    global current_user
    current_user = username

def header(title):
    """Print a formatted header"""
    clear_terminal()
    print(f"{title}")
    print(f"Přihlášen uživatel: {current_user}\n")
    print("SOFTWARE PRO SMĚNÁRNY - by Kučera")
    print("!!! Tato aplikace je ve vývoji, některé funkce nemusí být implementovány !!! \n")
    

def load_json(file_path):
    """Loads a JSON file and returns its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        save_json(file_path, [])  # Create an empty JSON file if it doesn't exist   
        return [] 
    except json.JSONDecodeError:
        print(f"Soubor {file_path} není platný JSON.")
        return []


def save_json(file_path, data):
    """Saves data to a JSON file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Chyba při ukládání souboru {file_path}: {e}")
        print(f"Data nebyla uložena !!!")
        
        
def add_transaction_log(t_type, amount, currency, balance_after):
    file_path = "cash_register_transactions.json"
    
    # Load existing history (if file does not exist, load_json returns [])
    history = load_json(file_path)
    
    # Create a new record
    new_record = {
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": t_type,
        "amount": amount,
        "currency": currency,
        "balance_after": balance_after,
        "user": current_user 
    }
    
    #  Adding to the list
    history.append(new_record)
    
    # Save back to the file
    save_json(file_path, history)