# Decorator to add a report header

def report_header(func):
    def wrapper(*args, **kwargs):

#wrapper() is an inner function. 2) *args and **kwargs allow it to accept any number of positional and keyword arguments.

      print("=" * 40)
      print(" STUDENT REPORT")
      print("=" * 40)
      func(*args, **kwargs)
      print("=" * 40)
    return wrapper


class Report:
    college = "MIT ADT University"

    # Constructor (Magic Method)
    def __init__(self, name, roll, marks):
      self.name = name
      self.roll = roll
      self.marks = marks

    # Class Method
    @classmethod
    def change_college(cls, new_name):
        cls.college = new_name

    # Magic Method
    def __str__(self):
        return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

    # Decorator applied to display report
    @report_header
    def display_report(self):
        print(f"College : {Report.college}")
        print(self)
        if self.marks >= 40:
            print("Result : PASS")
        else:
            print("Result : FAIL")

# Main Program
student1 = Report("Manoj", 1, 85)
student1.display_report()
print()

# Change college name using class method
Report.change_college("Massachusetts Institute of Technology")
student2 = Report("Kanya", 2, 35)
student2.display_report()


# Output

'''========================================
 STUDENT REPORT
========================================
College : MIT ADT University
Name : Manoj
Roll No : 1
Marks : 85
Result : PASS
========================================

========================================
 STUDENT REPORT
========================================
College : Massachusetts Institute of Technology
Name : Kanya
Roll No : 2
Marks : 35
Result : FAIL
========================================'''