from utils import header, continue_prompt, load_json, save_json
import getpass
import bcrypt


def next_user():
    header("Nový uživatel")
    file_path = "user.json"
    users = load_json(file_path)
    new_user_name = input("Napiš uživatelské jméno: ").strip()
    if not new_user_name:
        print("Chyba: Uživatelské jméno nesmí být prázdné.")
        return
    
    if any(u['username'] == new_user_name for u in users):
        print("Chyba: Toto uživatelské jméno už existuje.")
        return
    for i in range(3):
        print(f"Pokus {i+1} z 3 pro vložení hesla:")
        new_user_pass = getpass.getpass("Napiš uživatelské heslo: ")
        if not new_user_pass:
            print("Chyba: Heslo nesmí být prázdné.")
            continue
        check_new_user_pass = getpass.getpass("Napiš uživatelské heslo znovu: ")

        if new_user_pass == check_new_user_pass:
            print("Hesla jsou v pořádku.")
            hashed_pw = bcrypt.hashpw(new_user_pass.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            users.append({
                "username" : new_user_name,
                "password_hash" : hashed_pw
            })
            save_json(file_path, users)
            print(f"Uživatel {new_user_name} byl úspěšně zaregistrován.")
            return
        print("Hesla nejsou stejná, zkus to znovu.")
    print("registrace selhala: Hesla se ani na 3 pokusy neshodovala.")
    continue_prompt()