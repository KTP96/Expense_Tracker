import json

file_name = "expense_list.json"

def create_expense(expense_list):
    while True:
        try:
            expense_count = int(input("How many expenses do you want to enter?"))
            if expense_count <= 0 :
                raise ValueError
                
        except ValueError as e:
            print("Please enter a positive whole number")
                
        else:
            for i in range(0,expense_count):
                expense_desc = input("Enter the Description:")
                while True:
                    try:
                        expense_amount = float(input(f"Enter the amount spent on {expense_desc}"))
                        if expense_amount <= 0:
                            raise ValueError
                    except ValueError as e:
                        print("Please enter a valid number")
    
                    else:
                        expense_category = input("Enter the Category of expense: ").strip().lower()
                        expense_list.append(
                            {
                                "expense_desc":expense_desc,
                                "expense_amt":expense_amount,
                                "expense_category":expense_category
                            }
                        )
                        break
            save_expenses(expense_list)
            break

def view_expenses(expense_list):
    print("Expenses:")
    total_amount = 0
    for expense in expense_list:
        print(f"{expense['expense_desc']} [{expense['expense_category']}]:{expense['expense_amt']:.2f}")
        total_amount += expense['expense_amt']
    print(f"Total expense amount entered is: {total_amount:.2f}")

def view_category_expenses(expense_list):
    category = input("Which category would you like to view ?").strip().lower()
    print(f"Expenses in {category}:")
    category_total = 0
    found = False
    for expense in expense_list:
        if expense['expense_category'] == category:
            print(f"{expense['expense_desc']} [{expense['expense_category']}]:{expense['expense_amt']:.2f}")
            category_total += expense["expense_amt"]
            found = True
    print(f"Category_Total: {category_total:.2f}") if found else print("No expenses found in this category")

def summarize_expenses(expense_list):

    if not expense_list:
        print("The expense list is empty")
        return
      
    expense_summary = calculate_category_totals(expense_list)

    print("Spending by category: ")
    total_spending = 0
    for category, total in expense_summary.items():
        total_spending += total
        print(f"{category} : {total:.2f} ")
       
    print()
    print(f"Total spending:{total_spending:.2f}")

def calculate_category_totals(expense_list):
    expense_summary={}
    for expense in expense_list:
        category = expense['expense_category']
        if category in expense_summary:
            expense_summary[category] += expense['expense_amt']
     
        else:
            expense_summary[category] = expense['expense_amt']
    return expense_summary

def load_expenses():
    try:
        with open(file_name, "r") as file:
            expense_list=json.load(file)
            return expense_list
                    
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with no expenses")
        return []

    except json.JSONDecodeError as e:
        print(f"{file_name} contains invalid JSON. Please fix it before continuing.")
        raise SystemExit(1)
    
def save_expenses(expense_list):
    with open(file_name, "w") as file:
        json.dump(expense_list,file,indent=2)

def delete_expenses(expense_list):
        if not expense_list:
            print("The expense list is empty")
            return
        
        else:
            for i, expense in enumerate(expense_list,1 ):
                print(f"{i}. {expense['expense_desc']}: {expense['expense_amt']:.2f}")
        
        while True:
            try:
                choice = int(input(f"Enter the expense number to delete (0 to cancel)"))
                if choice > 0 and choice <= len(expense_list):
                    delete_expense = expense_list[choice - 1]
                    expense_list.pop(choice - 1 )
                    save_expenses(expense_list)
                    print(f"{delete_expense['expense_desc']} expense is deleted")

                elif choice == 0:
                    print("Deletion Cancelled")
                
                else:
                    raise ValueError
                
            except ValueError:
                print("Please enter a valid number from the list of expenses")

            else:
                break

def main(expenses):
    while True:
        option = input(f"\nExpense Tracker \n1. Add an expense \n2. View all expenses\n3. Filter by category\n4. Delete an expense \n5. Expense summary by category \n6. Exit  \n\nChoose an option:")

        if option == "1":
            create_expense(expenses)

        elif option == "2":
            if not expenses:
                print("No expenses recorded yet")
            else:
                view_expenses(expenses)

        elif option == "3":
            view_category_expenses(expenses)

        elif option == "4":
            delete_expenses(expenses)

        elif option == "5":
            summarize_expenses(expenses)

        elif option == "6":
            break
        
        else:
            print("Invalid Option. Please try again")

if __name__=="__main__":
    expenses = load_expenses()
    main(expenses)
