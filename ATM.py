from datetime import datetime

FILE = "atm_data.txt"


# ---------------- ACCOUNT FUNCTIONS ----------------

def create_account():
    print("\n--- CREATE ACCOUNT ---")
    acc = int(input("Enter account number: "))
    name = input("Enter name: ")
    dob =int(input("Enter DOB (DD-MM-YYYY): "))
    bal = float(input("Enter opening balance: "))

    with open(FILE, "a") as f:
        f.write(f"{acc}|{name}|{dob}|{bal}\n")

    print("Account created successfully.")


def login():
    acc = input("Enter account number: ")
    dob = input("Enter DOB: ")

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")

            if data[0] == acc and data[2] == dob:
                print("Login successful")
                second_menu(acc)
                return

    print("Invalid login details")
def get_balance(acc):
    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == acc:
                return float(data[3])
    return 0


def update_balance(acc, new_balance):
    lines = []
    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")

            if data[0] == acc:
                data[3] = str(new_balance)
                line = "|".join(data) + "\n"

            lines.append(line)

    with open(FILE, "w") as f:
        f.writelines(lines)


# ---------------- TRANSACTIONS ----------------

def add_transaction(acc, t_type, amount, balance):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(FILE, "a") as f:
        f.write(f"T|{acc}|{t_type}|{amount}|{now}|{balance}\n")


def deposit(acc):
    amount = float(input("Enter amount to deposit: "))
    bal = get_balance(acc)

    bal += amount
    update_balance(acc, bal)
    add_transaction(acc, "CREDIT", amount, bal)

    print("Amount credited. New balance:", bal)


def withdraw(acc):
    amount = float(input("Enter amount to withdraw: "))
    bal = get_balance(acc)

    if amount > bal:
        print("Insufficient balance")
        return

    bal -= amount
    update_balance(acc, bal)
    add_transaction(acc, "DEBIT", amount, bal)

    print("Amount debited. New balance:", bal)


# ---------------- HISTORY ----------------

def transaction_history(acc):
    print("\n--- TRANSACTION HISTORY ---")

    with open(FILE, "r") as f:
        found = False
        for line in f:
            data = line.strip().split("|")

            if data[0] == "T" and data[1] == acc:
                found = True
                print("\nType:", data[1])
                print("Amount:", data[2])
                print("Date:", data[3])
                print("Balance:", data[4])

        if not found:
            print("No transactions found.")


def mini_statement(acc):
    print("\n--- MINI STATEMENT (LAST 3) ---")

    transactions = []

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split("|")

            if data[0] == "T" and data[1] == acc:
                transactions.append(data)

    last3 = transactions[-3:]

    for t in last3:
        print("\nType:", t[1])
        print("Amount:", t[2])
        print("Date:", t[3])
        print("Balance:", t[4])
def show_account_details(acc):
    with open("atm_data.txt", "r") as f:
        for line in f:
            data = line.strip().split("|")

            # Skip transaction lines
            if data[0] == "T":
                continue

            if data[0] == acc:
                print("\n--- ACCOUNT HOLDER DETAILS ---")
                print("Account Number :", data[0])
                print("Name           :", data[1])
                print("Date of Birth  :", data[2])
                print("Balance        :", data[3])
                return

    print("Account not found")
# ---------------- SECOND MENU ----------------

def second_menu(acc):
    while True:
        print("\n===== TRANSACTION MENU =====")
        print("1. Check Balance")
        print("2. Deposit (Credit)")
        print("3. Withdraw (Debit)")
        print("4. Transaction History")
        print("5. Mini Statement")
        print("6. Account details")
        print("7. Logout")

        ch = input("Enter choice: ")

        if ch == "1":
            print("Balance:", get_balance(acc))

        elif ch == "2":
            deposit(acc)

        elif ch == "3":
            withdraw(acc)

        elif ch == "4":
            transaction_history(acc)

        elif ch == "5":
            mini_statement(acc)

        elif ch == "6":
            show_account_details(acc)
        elif ch=="7":
            break
        else:
            print("Invalid choice")
def main():
    while True:
        print("\n===== ATM SYSTEM =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            create_account()

        elif ch == "2":
            login()

        elif ch == "3":
            break

        else:
            print("Invalid choice")


main()