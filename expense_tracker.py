class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount):
        expense = {"name": name, "amount": amount}
        self.expenses.append(expense)
        print("Expense added!")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses yet.")
            return
        for expense in self.expenses:
            print(expense["name"], "-", expense["amount"])

    def get_total(self):
        total = 0
        for expense in self.expenses:
            total = total + expense["amount"]
        return total

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for expense in self.expenses:
                file.write(expense["name"] + "," + str(expense["amount"]) + "\n")
        print("Expenses saved!")

    def load_expenses(self):
        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    if line.strip() == "":
                        continue
                    parts = line.strip().split(",")
                    self.expenses.append({"name": parts[0], "amount": float(parts[1])})
        except FileNotFoundError:
            print("No saved expenses found. Starting fresh.")


def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Save and exit")
        choice = input("Choose 1-4: ")

        if choice == "1":
            name = input("What did you buy? ")
            try:
                amount = float(input("How much? "))
            except ValueError:
                print("Please type a number.")
                continue
            tracker.add_expense(name, amount)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            print("Total spent:", tracker.get_total())
        elif choice == "4":
            tracker.save_expenses()
            break
        else:
            print("Please choose 1, 2, 3 or 4.")


main()