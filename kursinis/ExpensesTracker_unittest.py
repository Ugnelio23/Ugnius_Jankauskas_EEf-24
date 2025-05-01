import unittest
from io import StringIO
from unittest.mock import patch
from ExpensesTracker import Expense, Income, ExpenseTracker  


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        """Išvalome singleton'ą prieš kiekvieną testą."""
        self.tracker = ExpenseTracker()
        self.tracker.expenses = []

    def test_add_expense(self):
        expense = Expense(date="2025-05-01", description="Coffee", amount=3.50)
        self.tracker.add_transaction(expense)
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertIsInstance(self.tracker.expenses[0], Expense)
        self.assertEqual(self.tracker.expenses[0].amount, 3.50)

    def test_add_income(self):
        income = Income(amount=1000.00)
        self.tracker.add_transaction(income)
        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertIsInstance(self.tracker.expenses[0], Income)
        self.assertEqual(self.tracker.expenses[0].amount, 1000.00)

    def test_remove_transaction(self):
        expense = Expense(date="2025-05-01", description="Lunch", amount=10.00)
        self.tracker.add_transaction(expense)
        self.tracker.remove_transaction(0)
        self.assertEqual(len(self.tracker.expenses), 0)

    def test_total_expenses(self):
        self.tracker.add_transaction(Expense("2025-05-01", "Lunch", 10.00))
        self.tracker.add_transaction(Expense("2025-05-02", "Movie", 15.00))
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.tracker.total_expenses()
        self.assertIn("Total expenses: €25.00", mock_stdout.getvalue())

    def test_total_income(self):
        self.tracker.add_transaction(Income(1000.00))
        self.tracker.add_transaction(Income(500.00))
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.tracker.total_income()
        self.assertIn("Total income: €1500.00", mock_stdout.getvalue())

    def test_balance(self):
        self.tracker.add_transaction(Expense("2025-05-01", "Lunch", 10.00))
        self.tracker.add_transaction(Income(1000.00))
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.tracker.balance()
        self.assertIn("Balance: €990.00", mock_stdout.getvalue())

    def test_save_and_load_file(self):
        self.tracker.add_transaction(Expense("2025-05-01", "Coffee", 3.50))
        self.tracker.add_transaction(Income(1000.00))
        self.tracker.save_to_file("test_expenses.csv")

        # Sukuriame naują objektą, bet išvalome jo sąrašą
        new_tracker = ExpenseTracker()
        new_tracker.expenses = []
        new_tracker.load_from_file("test_expenses.csv")

        self.assertEqual(len(new_tracker.expenses), 2)
        self.assertIsInstance(new_tracker.expenses[0], Expense)
        self.assertIsInstance(new_tracker.expenses[1], Income)

    def test_invalid_remove_transaction(self):
        self.tracker.add_transaction(Expense("2025-05-01", "Lunch", 10.00))
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.tracker.remove_transaction(5)  # Netinkamas indeksas
        self.assertIn("Invalid index.", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()

