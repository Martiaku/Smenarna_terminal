
from utils import header, continue_prompt, clear_terminal, load_json
from home_page import home_page
import getpass
import bcrypt

def login():
    users = load_json("user.json")
    for i in range(3):
        clear_terminal()
        header("Přihlášení")
        print(f"Pokus {i+1} z 3:")
        
        username = input("Uživatelské jméno: ")
        password = getpass.getpass("Heslo: ")

        # Check if the user exists and the password is correct
        user = next((u for u in users if u["username"] == username), None)
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password_hash"].encode('utf-8')):
            print("\n Přihlášení proběhlo úspěšně!")
            continue_prompt()
            home_page()
            return
        else:
            print("\n Neplatné jméno nebo heslo")
            continue_prompt()

    print("Příliš mnoho neúspěšných pokusů. Přístup zamítnut.")

if __name__ == "__main__":
    login()
