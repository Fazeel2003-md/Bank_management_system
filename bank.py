account = {
    1001: {'name': 'fazeel', 'balance': 4500, 'pin': 5042, 'history': []},
    1002: {'name': 'nazeer', 'balance': 5000, 'pin': 3012, 'history': []}
}
def verify_pin(acc_num):
    attempts = 3
    while attempts > 0:
        try:
            pin_num = int(input("Enter your PIN: "))
        except ValueError:
            print("Invalid input. Enter numbers only.")
            continue

        if account[acc_num]['pin'] == pin_num:
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")

    print("Too many wrong attempts. Access denied.")
    return False

def record_transaction(acc_num, message):
    account[acc_num]['history'].append(message)

    # Keep only last 5 transactions
    if len(account[acc_num]['history']) > 5:
        account[acc_num]['history'].pop(0)

def create_account():
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if acc_num in account:
        print("Account already exists.")
        return

    name = input("Enter name: ")

    try:
        balance = int(input("Enter initial deposit: "))
        if balance < 0:
            print("Balance cannot be negative.")
            return
    except ValueError:
        print("Invalid balance amount.")
        return

    try:
        pin = int(input("Set 4-digit PIN: "))
        if len(str(pin)) != 4:
            print("PIN must be 4 digits.")
            return
    except ValueError:
        print("Invalid PIN.")
        return

    account[acc_num] = {
        'name': name,
        'balance': balance,
        'pin': pin,
        'history': []
    }

    print("Account created successfully!")


def view_account():
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if acc_num not in account:
        print("Account not found.")
        return

    if verify_pin(acc_num):
        details = account[acc_num]
        print("\n--- Account Details ---")
        print("Account Number:", acc_num)
        print("Name:", details['name'])
        print("Balance:", details['balance'])


def deposit_money():
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if acc_num not in account:
        print("Account not found.")
        return

    if verify_pin(acc_num):
        try:
            amount = int(input("Enter deposit amount: "))
            if amount <= 0:
                print("Enter valid deposit amount.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        account[acc_num]['balance'] += amount
        record_transaction(acc_num, f"Deposited {amount}")
        print("Deposit successful. Updated balance:", account[acc_num]['balance'])


def withdraw_money():
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if acc_num not in account:
        print("Account not found.")
        return

    if verify_pin(acc_num):
        try:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Enter valid withdrawal amount.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        if amount > account[acc_num]['balance']:
            print("Insufficient balance.")
            return

        account[acc_num]['balance'] -= amount
        record_transaction(acc_num, f"Withdrawn {amount}")
        print("Withdrawal successful. Updated balance:", account[acc_num]['balance'])


def delete_account():
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if acc_num not in account:
        print("Account not found.")
        return

    if verify_pin(acc_num):
        account.pop(acc_num)
        print("Account deleted successfully.")


def transaction_history():
    try:
        acc_num = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if acc_num not in account:
        print("Account not found.")
        return

    if verify_pin(acc_num):
        history = account[acc_num]['history']

        if not history:
            print("No transactions yet.")
        else:
            print("\n--- Last Transactions ---")
            for t in history:
                print(t)

def main_menu():
    while True:
        print("\n------ Bank Management System ------")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Delete Account")
        print("6. Transaction History")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            view_account()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            withdraw_money()
        elif choice == '5':
            delete_account()
        elif choice == '6':
            transaction_history()
        elif choice == '7':
            print("Thank you for visiting our bank!")
            break
        else:
            print("Invalid choice.")


main_menu()
