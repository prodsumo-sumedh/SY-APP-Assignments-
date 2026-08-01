class Course:
    def __init__(self,course_name,duration,fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

    def Course_Category(self):
        if self.duration <=1:
            return "Short term course category"
        else:
            return "Long term course category "

    def Display(self):
        print(f"{self.course_name:<20} {self.duration:<15} {self.fees:<20} {self.Course_Category()}")

class Institute:
    def __init__(self,name):
        self.name = name
        self.courses =[]


    def Add_courses(self,course_name,duration,fees):
        course= Course(course_name,duration,fees)
        self.courses.append(course)
        print(f"Course added successfully: {course_name} -{duration}(in years)")

    def display(self):
        print(f"========== {self.name} =========")
        print(f"{'Course':<20} {'Duration(years)':<15} {'Fees':<20} {'Category'}")
        for cour in self.courses:
            cour.Display()

institute = Institute("MIT ADT UNIVERSITY")
institute.Add_courses("BTech in CSE",4,1272000)
institute.Add_courses("IBM Data science",0.3,6000)
institute.Add_courses("BBA",3,900000)

institute.display()