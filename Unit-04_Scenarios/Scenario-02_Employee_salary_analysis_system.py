import numpy as np
import pandas as pd

def main():
    print("=== Employee Salary Analysis ===\n")
    
    # Create a NumPy array of employee salaries
    salaries = np.array([45000, 62000, 78000, 54000, 85000, 59000, 92000, 48000])
    
    # Calculate average, maximum, and minimum salary
    print("--- Salary Statistics (NumPy) ---")
    print(f"Average Salary : ₹{np.mean(salaries):,.2f}")
    print(f"Maximum Salary : ₹{np.max(salaries):,}")
    print(f"Minimum Salary : ₹{np.min(salaries):,}")
    
    # Create a Pandas DataFrame
    data = {
        'EmpID': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008'],
        'Name': ['Aarav', 'Priya', 'Vikram', 'Neha', 'Rohan', 'Sanya', 'Arjun', 'Meera'],
        'Salary': salaries
    }
    df = pd.DataFrame(data)
    
    print("\n--- Full Employee Records ---")
    print(df.to_string(index=False))
    
    # Display employees earning more than ₹60,000
    print("\n--- Employees Earning More Than ₹60,000 ---")
    high_earners = df[df['Salary'] > 60000]
    
    if not high_earners.empty:
        print(high_earners.to_string(index=False))
    else:
        print("No employees earn more than ₹60,000.")

if __name__ == "__main__":
    main()
