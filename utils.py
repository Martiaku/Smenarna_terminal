

# This file contains "helper functions"

import os
import json

def clear_terminal():
    """Clear the console"""
    os.system("cls" if os.name == "nt" else "clear")
    
    
def continue_prompt():
    input("Stiskni Enter pro pokračování...")


def header(title):
    """Print a formatted header"""
    clear_terminal()
    print(f"{title}")
    print("SOFTWARE PRO SMĚNÁRNY - by Kučera")
    print("!!! Táto aplikace je ve vývoji, některé funkce nemusí být implementovány !!! \n")
    

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