import json
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
    
    def add_expense(self, amount, category, description):
        next_id = max(self.expenses.keys(), default=0) + 1
        self.expenses[next_id] = {
            'amount': amount,
            'category': category,
            'description': description
        }
        print(f"\n Added expense ID {next_id}: ${amount} for {category}")
    
    def view_expenses(self):
        if not self.expenses:
            print("\n No expenses recorded yet.")
            return

        print(f"\n{'ID':<5} {'Amount':<10} {'Category':<15} {'Description'}")
        print("-" * 50)
        
        total = 0
        for exp_id, details in self.expenses.items():
            print(f"{exp_id:<5} ${details['amount']:<9} {details['category']:<15} {details['description']}")
            total += details['amount']
        
        print("-" * 50)
        print(f"{'TOTAL':<5} ${total:<9}")
    
    def filter_by_category(self, cat):
        print(f"\n🔍 Filtering for: {cat}")
        print(f"{'ID':<5} {'Amount':<10} {'Category':<15} {'Description'}")
        print("-" * 50)
        found = False
        for exp_id, details in self.expenses.items():
            if details['category'].lower() == cat.lower():
                print(f"{exp_id:<5} ${details['amount']:<9} {details['category']:<15} {details['description']}")
                found = True
        if not found:
            print("No expenses found in this category.")

# --- Menu System Implementation ---

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n---  Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            try:
                amt = float(input("Enter amount: "))
                cat = input("Enter category: ")
                desc = input("Enter description: ")
                tracker.add_expense(amt, cat, desc)
            except ValueError:
                print(" Invalid input. Please enter a number for the amount.")

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            category_to_find = input("Enter category name to filter by: ")
            tracker.filter_by_category(category_to_find)

        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
        

             




ok = ExpenseTracker()
wow = ok.add_expense(50, "Uber", "More travel to buy")
wow = ok.add_expense(50, "Food", "More food to buy")
print(ok.filter("Food"))


