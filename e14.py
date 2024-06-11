class User:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive amount.")
        else:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. Your new balance is ${self.balance:.2f}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. Your new balance is ${self.balance:.2f}.")

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin


class ATM:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def authenticate_user(self):
        attempts = 3
        while attempts > 0:
            name = input("Please enter your name: ")
            pin = input("Please enter your PIN: ")

            for user in self.users:
                if user.name == name and user.verify_pin(pin):
                    print("Authentication successful.")
                    return user

            attempts -= 1
            print(f"Incorrect name or PIN. You have {attempts} attempts left.")

        print("Too many incorrect attempts. Exiting.")
        return None

    def main_menu(self, user):
        while True:
            print(f"\n--- ATM Transaction for {user.name} ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                print(f"Your current balance is: ${user.check_balance():.2f}")
            elif choice == '2':
                amount = float(input("Enter the amount to deposit: $"))
                user.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: $"))
                user.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    atm = ATM()

    atm.add_user(User("Alice", "1111", 1000))
    atm.add_user(User("Bob", "2222", 1500))
    atm.add_user(User("Charlie", "3333", 500))

    user = atm.authenticate_user()
    if user:
        atm.main_menu(user)


if __name__ == "__main__":
    main()
