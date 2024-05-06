# Define a function to add an expense to the list
def add_expense(expenses, amount, category):
    # Append a new expense to the list as a dictionary
    expenses.append({'amount': amount, 'category': category})

# Define a function to print all expenses
def print_expenses(expenses):
    # Iterate over each expense in the list
    for expense in expenses:
        # Print the amount and category of each expense
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Define a function to calculate the total of all expenses
def total_expenses(expenses):
    # Use a lambda function to extract the amount from each expense
    # and sum them up using the built-in sum function
    return sum(map(lambda expense: expense['amount'], expenses))

# Define a function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    # Use a lambda function to filter expenses based on the category
    # and return the filtered list
    return filter(lambda expense: expense['category'] == category, expenses)

# Define the main function
def main():
    # Initialize an empty list to store expenses
    expenses = []
    # Loop indefinitely until the user chooses to exit
    while True:
        # Print the menu
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        # Get the user's choice
        choice = input('Enter your choice: ')

        # Handle each choice
        if choice == '1':
            # Get the amount and category from the user
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            # Add the expense to the list
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Print all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            # Print the total of all expenses
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            # Get the category to filter by from the user
            category = input('Enter category to filter: ')
            # Filter expenses by category and print the result
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break

# Run the main function if this script is executed directly
if __name__ == '__main__':
    main()