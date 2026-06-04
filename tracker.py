import json
import os

# File to store expenses permanently
DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def main():
    expenses_list = load_expenses()
    print("=== Welcome to Personal Expense Tracker ===")
    
    while True:
        print("\n" + "="*10 + " MENU " + "="*10)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. Exit")
        
        choice = input("Please Enter Your Choice (1-4): ").strip()
        
        if choice == "1":
            date = input("Enter date (DD-MM-YYYY): ")
            category = input("Enter category (Food, Travel, Makeup, Books, etc.): ")
            description = input("Enter description: ")
            
            try:
                amount = float(input("Enter the amount: "))
            except ValueError:
                print("❌ Invalid amount! Please enter a numeric value.")
                continue
                
            expense = {
                "date": date,
                "category": category,
                "description": description,
                "amount": amount
            }
            
            expenses_list.append(expense)
            save_expenses(expenses_list)
            print("✅ Success: Expense added successfully!")
            
        elif choice == "2":
            if not expenses_list:
                print("ℹ️ No expenses recorded yet.")
            else:
                print("\n--- All Expenses ---")
                for index, exp in enumerate(expenses_list, 1):
                    print(f"{index}. Date: {exp['date']} | Category: {exp['category']} | Desc: {exp['description']} | Amount: ₹{exp['amount']}")
                    
        elif choice == "3":
            total = sum(exp['amount'] for exp in expenses_list)
            print(f"\n📊 TOTAL SPENDING: ₹{total:.2f}")
            
        elif choice == "4":
            print("Thank you for using the Expense Tracker System. Goodbye!")
            break
            
        else:
            print("❌ INVALID CHOICE. PLEASE TRY AGAIN.")

if __name__ == "__main__":
    main()