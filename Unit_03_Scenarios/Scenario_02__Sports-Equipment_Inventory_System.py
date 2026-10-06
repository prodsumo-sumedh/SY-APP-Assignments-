import csv
import sys

def load_equipment(filename):
    """Reads equipment records from the provided CSV file."""
    equipment_list = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                equipment_list.append(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)
        
    return equipment_list

def display_all(equipment_list):
    """Displays all equipment records in a formatted table."""
    if not equipment_list:
        print("No equipment records found in the file.")
        return

    print("\n--- All Sports Equipment ---")
    headers = equipment_list[0].keys()
    
    # Print headers
    print(" | ".join(f"{header:<15}" for header in headers))
    print("-" * 75)
    
    # Print rows
    for item in equipment_list:
        print(" | ".join(f"{value:<15}" for value in item.values()))
    print("-" * 75)

def search_equipment(equipment_list):
    """Searches for a specific piece of equipment using Equipment ID."""
    search_id = input("\nEnter Equipment ID to search: ").strip()
    
    for item in equipment_list:
        # Assumes the CSV has a column named 'EquipmentID'
        if item.get('EquipmentID') == search_id:
            print("\n--- Equipment Found ---")
            for key, value in item.items():
                print(f"{key:>15}: {value}")
            return
            
    print(f"\nNo equipment found with ID: {search_id}")

def main():
    # Requirement: Accept filename using command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python app.py <filename.csv>")
        print("Example: python app.py sports.csv")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    # Requirement: Read equipment details
    equipment_list = load_equipment(filename)
    
    while True:
        print("\n=== Sports Equipment Manager ===")
        print("1. Display All Equipment")
        print("2. Search by Equipment ID")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            display_all(equipment_list)
        elif choice == '2':
            search_equipment(equipment_list)
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
