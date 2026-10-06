import csv
import re
import sys

# Define the expected account number format (exactly 10 digits)
ACCOUNT_REGEX = r'^\d{10}$'
CSV_FILE = 'customers.csv'

def validate_account_number(acc_num):
    """Validates the account number using regex."""
    return bool(re.match(ACCOUNT_REGEX, acc_num))

def load_customers(filename):
    """Reads customer records from the CSV file."""
    customers = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                customers.append(row)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please create the file and try again.")
        sys.exit(1)
    return customers

def display_all_customers(customers):
    """Displays all customer records in a formatted table."""
    if not customers:
        print("No customer records found.")
        return
    
    print("\n--- All Customer Details ---")
    headers = customers[0].keys()
    
    # Print header row
    print(" | ".join(f"{header:<15}" for header in headers))
    print("-" * 65)
    
    # Print data rows
    for cust in customers:
        print(" | ".join(f"{value:<15}" for value in cust.values()))
    print("-" * 65)

def search_customer(customers):
  
    acc_num = input("\nEnter 10-digit Account Number to search: ").strip()
    
    # Requirement: Validate using Regular Expressions
    if not validate_account_number(acc_num):
        print("Error: Invalid format! Account Number must be exactly 10 digits.")
        return

    # Requirement: Search and display
    for cust in customers:
        # Assumes the CSV has a column exactly named 'AccountNumber'
        if cust.get('AccountNumber') == acc_num:
            print("\n--- Customer Found ---")
            for key, value in cust.items():
                print(f"{key:>15}: {value}")
            return
            
    print("\nNo customer found with that Account Number.")

def main():
    # Requirement: Read customer records
    customers = load_customers(CSV_FILE)
    
    while True:
        print("\n=== Customer Account Management ===")
        print("1. Display All Customers")
        print("2. Search Customer by Account Number")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            display_all_customers(customers)
        elif choice == '2':
            search_customer(customers)
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
