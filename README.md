# Python Terminal Login & Registration System

## English

Simple terminal app for user login, registration, and basic exchange-office menu flows.

### Features
- Secure password storage using `bcrypt` (no plain-text passwords).
- User data stored in `user.json`.
- Attempt limit (3 tries) for login and password confirmation during registration.
- Modular project structure (`login.py`, `next_user.py`, `utils.py`, `home_page.py`).

### Requirements
- Python 3.10+
- Dependencies listed in `requirements.txt`

### Installation
```bash
pip install -r requirements.txt
```

### Run
Login flow:
```bash
python login.py
```

New user registration:
```bash
python next_user.py
```

### Project Structure
- `login.py` - user authentication
- `next_user.py` - new user registration
- `home_page.py` - main menu after successful login
- `utils.py` - helper functions (headers, JSON, terminal)
- `transfer_money.py` - basic currency conversion
- `currency_rates.py` - currency rates and mapping
- `validation.py` - input validation functions
- `user.json` - local user database (should stay ignored in git)
- `withdraw_money.py` - Withdraw money from the cash register
- `deposit_money.py` - Deposit money into the cash register
- `transaction_history.py` - View transaction history
- `cash_register.json` - Cash register status (should be ignored in git)
- `cash_register_transactions.json` - Transaction history log (should be ignored in git)

### Security Notes
- Passwords are hashed with `bcrypt`.
- Do not commit `user.json` to a public repository.

---

## Čeština

Jednoduchá terminálová aplikace pro přihlášení, registraci uživatele a základní menu směnárny.

### Funkce
- Bezpečné ukládání hesel pomocí `bcrypt` (žádná hesla v čistém textu).
- Ukládání uživatelů do `user.json`.
- Omezení pokusů na 3 při přihlášení i při potvrzení hesla při registraci.
- Modulární struktura projektu (`login.py`, `next_user.py`, `utils.py`, `home_page.py`).

### Požadavky
- Python 3.10+
- Závislosti uvedené v `requirements.txt`

### Instalace
```bash
pip install -r requirements.txt
```

### Spuštění
Přihlášení:
```bash
python login.py
```

Registrace nového uživatele:
```bash
python next_user.py
```

### Struktura projektu
- `login.py` - autentizace uživatele
- `next_user.py` - registrace nového uživatele
- `home_page.py` - hlavní menu po úspěšném přihlášení
- `utils.py` - pomocné funkce (hlavičky, JSON, terminál)
- `transfer_money.py` - základní převod měn
- `currency_rates.py` - kurzy a mapování měn
- `validation.py` - validační funkce vstupu
- `user.json` - lokální databáze uživatelů (měla by zůstat ignorovaná v git)
- `withdraw_money.py` - Výběr peněz z pokladny
- `deposit_money.py` - Vklad peněz do pokladny
- `transaction_history.py` - Pohlížení historie transakcí
- `cash_register.json` - Stav financí v pokladně (měla by zůstat ignorovaná v git)
- `cash_register_transactions.json` - Log historie transakcí (měl by zůstat ignorovaná v git)

### Bezpečnost
- Hesla jsou hashovaná pomocí `bcrypt`.
- `user.json` necommitovat do veřejného repozitáře.
