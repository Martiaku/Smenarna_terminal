from utils import header, continue_prompt, load_json, save_json

import bcrypt

# Function for secure user password update.

def change_password():
    header("Změna hesla")
    file_path = "users.json"
    
    # 1. We load the data into a variable ONCE
    all_users = load_json(file_path)
    print("Uživatelé v systému:")
    for user in all_users:
        print(f"{user['username']}")
    
    username = input("Zadejte své uživatelské jméno: ")
    current_password = input("Zadejte své současné heslo: ")

    # 2. We find the user in the loaded data
    user = next((u for u in all_users if u["username"] == username), None)

    # 3. Verification (bcrypt)
    if user and bcrypt.checkpw(current_password.encode('utf-8'), user["password_hash"].encode('utf-8')):
        new_password = input("Zadejte nové heslo: ")
        confirm_password = input("Potvrďte nové heslo: ")

        if new_password == confirm_password:
            # 4. We change the hash directly in the object that is part of the all_users list
            hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user["password_hash"] = hashed
            
            # 5. We save the entire modified list back
            save_json(file_path, all_users)
            print(" Heslo bylo úspěšně změněno.")
        else:
            print(" Hesla se neshodují.")
    else:
        print(" Neplatné uživatelské jméno nebo heslo.")
    
    continue_prompt()