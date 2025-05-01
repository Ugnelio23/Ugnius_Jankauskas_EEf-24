import datetime
import csv


class Transaction:
    """Base class for all transactions like Expense and Income."""
    def get_summary(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Expense(Transaction):
    def __init__(self, date, description, amount):
        self._date = date
        self._description = description
        self._amount = amount

    @property
    def date(self):
        return self._date

    @property
    def description(self):
        return self._description

    @property
    def amount(self):
        return self._amount

    def get_summary(self):
        return f"Expense on {self._date}: {self._description} - €{self._amount}"


class Income(Transaction):
    def __init__(self, amount, date=None):
        self._date = date if date else datetime.datetime.now().strftime("%Y-%m-%d")  # Default to today's date
        self._description = "Income entry"  # Default description
        self._amount = amount

    @property
    def date(self):
        return self._date

    @property
    def description(self):
        return self._description

    @property
    def amount(self):
        return self._amount

    def get_summary(self):
        return f"Income on {self._date}: {self._description} + €{self._amount}"


class ExpenseTracker:
    """Singleton class to manage expenses and income."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.expenses = []
        return cls._instance

    def add_transaction(self, transaction):
        """Add an expense or income to the tracker."""
        self.expenses.append(transaction)

    def remove_transaction(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            print("Invalid index.")

    def view_transactions(self):
        if not self.expenses:
            print("No transactions found.")
        else:
            for idx, transaction in enumerate(self.expenses, start=1):
                print(f"{idx}. {transaction.get_summary()}")

    def total_expenses(self):
        """Calculate and print the total sum of all expenses."""
        total = sum(transaction.amount for transaction in self.expenses if isinstance(transaction, Expense))
        print(f"Total expenses: €{total:.2f}")

    def total_income(self):
        """Calculate and print the total sum of all incomes."""
        total = sum(transaction.amount for transaction in self.expenses if isinstance(transaction, Income))
        print(f"Total income: €{total:.2f}")

    def balance(self):
        """Calculate and print the balance after transactions."""
        total_expenses = sum(transaction.amount for transaction in self.expenses if isinstance(transaction, Expense))
        total_income = sum(transaction.amount for transaction in self.expenses if isinstance(transaction, Income))
        balance = total_income - total_expenses
        print(f"Balance: €{balance:.2f}")

    def save_to_file(self, filename="expenses.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Date", "Description", "Amount"])
            for transaction in self.expenses:
                writer.writerow([transaction.__class__.__name__, transaction.date, transaction.description, transaction.amount])

    def load_from_file(self, filename="expenses.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    if row[0] == "Expense":
                        self.add_transaction(Expense(row[1], row[2], float(row[3])))
                    elif row[0] == "Income":
                        self.add_transaction(Income(float(row[3])))
        except FileNotFoundError:
            print("File not found, starting with empty data.")


def main():
    tracker = ExpenseTracker()
    tracker.load_from_file()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Remove Transaction")
        print("4. View Transactions")
        print("5. Total Expenses")
        print("6. View Balance")
        print("7. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            expense = Expense(date, description, amount)
            tracker.add_transaction(expense)
            print("Expense added successfully!")
        
        elif choice == "2":
            amount = float(input("Enter the income amount: "))
            income = Income(amount)
            tracker.add_transaction(income)
            print("Income added successfully!")

        elif choice == "3":
            index = int(input("Enter the index of the transaction to remove: "))
            tracker.remove_transaction(index - 1)

        elif choice == "4":
            tracker.view_transactions()

        elif choice == "5":
            tracker.total_expenses()

        elif choice == "6":
            tracker.balance()  # Option 6 shows the balance after transactions

        elif choice == "7":
            tracker.save_to_file()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()