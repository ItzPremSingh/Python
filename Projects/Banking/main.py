from getpass import getpass

from modals import User, UserAccount
from sql import conn, cursor


def register() -> None:
    username = input("Enter a username: ")
    password = getpass("Enter a password: ")
    confirm_password = getpass("Confirm password: ")

    if password == confirm_password:
        user = User(username, password)
        if user.register():
            print("Registration successful!")

        else:
            print("Username already exists. Registration failed.")
    else:
        print("Passwords do not match. Registration failed.")


def login() -> None:
    username = input("Enter your username: ")

    user = User(username)

    if not user.isRegistered():
        print("User does not exist. Login failed.")
        return

    if not user.isUnlocked():
        if lockOut := user.getLoginLockout():
            print(
                f"Your account is locked until {lockOut.strftime('%Y-%m-%d %H:%M:%S')}"
            )
        return

    if user.getLoginLockout():
        if user.isUnlocked():
            user.unlock()

    user.password = getpass("Enter your password: ")

    if user.isAuthenticated():
        userAccount = UserAccount(username)
        print("Login successful!")
        print(f"Welcome, {username}!")

        while True:
            print("1. View balance")
            print("2. Deposit funds")
            print("3. Withdraw funds")
            print("4. Transfer funds")
            print("5. View transaction history")
            print("6. Logout")
            print("7. Exit")

            try:
                choice = input("Enter your choice: ")
            except (KeyboardInterrupt, EOFError):
                print("Exiting...")
                return

            if choice == "1":
                print(f"Balance: {userAccount.getBalance()}")

            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                if amount <= 0:
                    print("Invalid deposit amount. Deposit failed.")
                    continue

                userAccount.deposit(amount)
                print(f"Deposit successful. New balance: {userAccount.getBalance()}")

            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Invalid withdrawal amount. Withdrawal failed.")
                    continue

                if userAccount.withdraw(amount):
                    print(
                        f"Withdrawal successful. New balance: {userAccount.getBalance()}"
                    )
                else:
                    print("Insufficient funds. Withdrawal failed.")

            elif choice == "4":
                username = input("Enter the username to transfer to: ")
                if username == userAccount.username:
                    print("You cannot transfer to yourself. Transfer failed.")
                    continue
                elif not User(username).isRegistered():
                    print("User does not exist. Transfer failed.")
                    continue

                amount = float(input("Enter the amount to transfer: "))
                if amount <= 0:
                    print("Invalid transfer amount. Transfer failed.")
                    continue

                if userAccount.transfer(username, amount):
                    print(
                        f"Transfer successful. New balance: {userAccount.getBalance()}"
                    )
                else:
                    print("Insufficient funds. Transfer failed.")

            elif choice == "5":
                for transaction in userAccount.getTransactionHistory():
                    print(
                        f"Amount: {transaction[0]}, Type: {transaction[1].capitalize()}, Date: {transaction[2]}"
                    )

            elif choice == "6":
                print("Logout successful.")
                return

            elif choice == "7":
                print("Goodbye!")
                conn.close()
                exit(0)

    else:
        user.increaseLoginAttempts()

        if user.getLoginAttempts() >= 3:
            user.lock()
            if lockOut := user.getLoginLockout():
                print(
                    f"Your account is locked until {lockOut.strftime('%Y-%m-%d %H:%M:%S')}"
                )
            return
        else:
            print(
                f"Invalid username or password. Login failed. Attempt(s) remaining: {3 - user.getLoginAttempts()}"
            )


def admin() -> None:
    if getpass("Enter the admin password: ") != "password":
        print("Invalid admin password. Access denied.")
        return

    print("Welcome, admin!")
    while True:
        print("1. View all users")
        print("2. View transactions for a specific user")
        print("3. Logout")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")
        except (KeyboardInterrupt, EOFError):
            print("Exiting...")
            return

        if choice == "1":
            for row in cursor.execute("SELECT username, balance FROM users"):
                print(f"Username: {row[0]}, Balance: {row[1]}")

        elif choice == "2":
            username = input("Enter the username: ")
            user = User(username)
            userAccount = UserAccount(username)

            if not user.isRegistered():
                print("User does not exist.")
                continue

            balance = userAccount.getBalance()
            print(f"Username: {username}, Balance: {balance}")

            for transaction in userAccount.getTransactionHistory():
                print(
                    f"Amount: {transaction[0]}, Type: {transaction[1].capitalize()}, Date: {transaction[2]}"
                )

        elif choice == "3":
            print("Logout successful.")
            return
        elif choice == "4":
            print("Goodbye!")
            conn.close()
            exit(0)
        else:
            print("Invalid choice. Please try again.")


def main() -> None:
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Admin")
        print("4. Exit")

        try:
            choice = input("Enter your choice: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            conn.close()
            exit(0)

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            admin()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
