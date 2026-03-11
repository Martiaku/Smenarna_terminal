

# This page contains "validation functions"

from datetime import date

def validation_yes_no(prompt):
    valid_yes = ["ano", "a"]
    valid_no = ["ne", "n"]
    while True:
        value = input(prompt).strip().lower()
        if value in valid_yes:
            return True
        if value in valid_no:
            return False
        print('Chyba: Odpovězte prosím "ano" nebo "ne". ' )
        

def validation_date(prompt):
    """Validates the date format (DD.MM.RRRR)."""
    while True:
        date_str = input(prompt)
        try:
            day, month, year = map(int, date_str.split('.'))
            date(year, month, day)  # This will raise ValueError if the date is invalid
            return date_str
        except ValueError:
            print("Neplatné datum!!! Zadejte datum ve formátu DD.MM.RRRR.")
            
def validation_float(prompt):
    """Validates that the input is a valid float number."""
    while True:
        value = input(prompt)
        if value.lower() == "q":
            return None
        try:
            return float(value)
        except ValueError:
            print("Neplatný vstup!!! Zadejte číslo (např. 100.50).")