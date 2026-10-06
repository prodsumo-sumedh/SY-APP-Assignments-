import numpy as np
import pandas as pd

def main():
    print("=== Student Marks Exploratory Data Analysis ===")
    
    # Create a NumPy array of student marks
    marks = np.array([45, 82, 91, 55, 78, 88, 62, 95, 73, 85])
    
    # Calculate mean, median, maximum, and minimum marks using NumPy
    print("\n--- Statistical Analysis (NumPy) ---")
    print(f"Mean (Average) : {np.mean(marks):.2f}")
    print(f"Median         : {np.median(marks)}")
    print(f"Maximum Marks  : {np.max(marks)}")
    print(f"Minimum Marks  : {np.min(marks)}")
    
    # Create a Pandas DataFrame from student records
    data = {
        'RollNo': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
        'Marks': marks
    }
    
    df = pd.DataFrame(data)
    
    print("\n--- Full Student Records DataFrame ---")
    print(df.to_string(index=False)) # to_string(index=False) hides the default row numbers for cleaner output
    
    # Display students scoring more than 80 marks
    print("\n--- Top Performers (Marks > 80) ---")
    top_students = df[df['Marks'] > 80]
    
    if not top_students.empty:
        print(top_students.to_string(index=False))
    else:
        print("No students scored more than 80 marks.")

if __name__ == "__main__":
    main()
