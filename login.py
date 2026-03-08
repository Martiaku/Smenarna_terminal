from utils import header, continue_prompt, clear_terminal, load_json, save_json
from home_page import home_page
import getpass
import bcrypt

# --- If users already exist in the database, do nothing ---
def ensure_default_admin(users, file_path):
    if users:
        return users
    # Create a default account (admin:admin) with a hashed password
    default_admin = {
        "username": "admin",
        "password_hash": bcrypt.hashpw("admin".encode("utf-8"), bcrypt.gensalt()).decode("utf-8"),
    }
    users = [default_admin]
    save_json(file_path, users)
    return users

# --- Main login process ---
def login():
    file_path = "user.json"
    users = load_json(file_path)
    # Validate the existence of the user database
    users = ensure_default_admin(users, file_path)
    # Limit to 3 attempts (to prevent brute-force attacks)
    for i in range(3):
        clear_terminal()
        header("Prihlaseni")
        print(f"Pokus {i + 1} z 3:")

        username = input("Uzivatelske jmeno: ")
        # Use getpass to hide password input
        password = getpass.getpass("Heslo: ")
        # Membership test - searching for the user in the list of users
        user = next((u for u in users if u["username"] == username), None)
        # Secure password verification using hash comparison
        if user and bcrypt.checkpw(password.encode("utf-8"), user["password_hash"].encode("utf-8")):
            print("\nPrihlaseni probehlo uspesne!")
            continue_prompt()
            home_page()
            return
        
        print("\nNeplatne jmeno nebo heslo")
        continue_prompt()
    # Response to exhausted attempts
    print("Prilis mnoho neuspesnych pokusu. Pristup zamitnut.")

# --- Entry point of the application ---
if __name__ == "__main__":
    login()
