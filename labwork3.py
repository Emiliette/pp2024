# Use math module to round-down student scores to 1-digit decimal upon input, floor()
# Use numpy module and its array to
# - Add function to calculate average GPA for a given student
# • Weighted sum of credits and marks
# - Sort student list by GPA descending
# Decorate your UI with curses module
import math
import numpy as np
import curses

class Class_Students: 
    def __init__(self):
        self.__id = input("Enter the student's ID: ")
        self.__name = input("Enter the student's Name: ")
        self.__dob = input("Enter the student's DoB: ")
        self.__mark = {}
        self.__gpa = 0.0

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

    # Save marks of students for the specific course
    def set_mark(self, course_id, mark):
        round_mark = math.floor(mark * 10) / 10
        # Eg: 19.88 -> 198.8 -> 198 -> 19.8
        self.__mark[course_id] = round_mark

    # Get marks of students for the specific course
    def get_mark(self, course_id):
        return self.__mark.get(course_id, None)
    
    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0.0

        for course in courses:
            course_id = course.get_id()
            if course_id in self.__mark:
                weighted_sum += self.__mark[course_id] * course.get_credits()
                total_credits += course.get_credits()
        
        if total_credits > 0:
            self.__gpa = weighted_sum / total_credits
        else: 
            self.__gpa = 0

    def get_gpa(self):
        return self.__gpa

class Class_Courses:
    def __init__(self):
        self.__id = input("Enter the course's ID: ")
        self.__name = input("Enter the course's name: ")
        self.__credits = int(input("Enter the course's credits: "))

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    
class Require:
    @staticmethod
    def input_something(args):
        return int(input(f"Enter the number of {args}: "))
    
    @staticmethod
    def show(something):
        # if not something:
        #     print(f"Invalid {something}.")

        for i, something in enumerate(something):
            print(f"{i+1}. ID: {something.get_id()} - Name: {something.get_name()} ") 
                    
class University:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []

    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    def set_num_students(self):
        self.__num_students = Require.input_something("students")

    def set_num_courses(self):
        self.__num_courses = Require.input_something("courses")

    def set_students(self):
        for _ in range(self.__num_students):
            self.__students.append(Class_Students())

    def set_courses(self):
        for _ in range(self.__num_courses):
            self.__courses.append(Class_Courses())

    def list_students(self):
        if not self.__students:
            print("The list of students is empty.")
        
        Require.show(self.__students)

    def list_courses(self):
        if not self.__courses:
            print("The lisst of courses is empty.")

        Require.show(self.__courses)

    def input_mark(self):
        course_id = input("Enter the course ID to input marks: ")

        if not any(course_id == a.get_id() for a in self.__courses):
            print("Invalid courses ID.")
            return

        for student in self.__students:
            mark = float(input(f"Enter the mark for {student.get_name()} - ID: {student.get_id()}: "))
            student.set_mark(course_id, mark)

    def show_mark(self):
        course_id = input("Enter the course ID you want to show: ")
        if not any(course_id == a.get_id() for a in self.__courses):
            print("Invalid course ID.")
            return

        for student in self.__students:
            mark = student.get_mark(course_id)
            print(f"ID: {student.get_id()}, Name: {student.get_name()}, Marks: {mark}")      
            
    def sort_gpa(self):
        # Calculate GPA for each student
        for student in self.__students:
            student.calculate_gpa(self.__courses)

        # Sort students by GPA in descending order
        gpa = np.array([student.get_gpa() for student in self.__students])
        sorted_index = np.argsort(gpa)[::-1]
        sorted_students = np.array(self.__students)[sorted_index]
        print("Students sorted by GPA in descending order:")
        for student in sorted_students:
            print(f"ID: {student.get_id()}, Name: {student.get_name()}, GPA: {student.get_gpa()}")


def main():
    university = University()

    while True: 
        print("""Choose the following options:
              0. Exit program
              1. Input number of students
              2. Input students' information
              3. Input number of courses
              4. Input courses' information
              5. Input marks for students in courses
              6. List courses
              7. List students
              8. Show marks for a given course
              9. List GPA of students""")
        
        option = int(input("Enter your choice: "))

        if option == 0:
            print("Exiting program. Goodbye!")
            break

        elif option == 1:
            university.set_num_students()

        elif option == 2:
            # university.set_num_students()
            university.set_students()

        elif option == 3:
            university.set_num_courses()

        elif option == 4:
            # university.set_num_courses()
            university.set_courses()

        elif option == 5:
            # university.set_num_students()
            # university.set_students()
            # university.set_num_courses()
            # university.set_courses()
            university.input_mark()

        elif option == 6:
            # university.set_num_courses()
            # university.set_courses()
            university.list_courses()

        elif option == 7: 
            # university.set_num_students()
            # university.set_students()
            university.list_students()

        elif option == 8:
            # university.set_num_students()
            # university.set_students()
            # university.set_num_courses()
            # university.set_courses()
            # university.input_mark()
            university.show_mark()
        
        elif option == 9:
            # university.set_num_students()
            # university.set_students()
            # university.set_num_courses()
            # university.set_courses()
            # university.input_mark()
            university.sort_gpa()

if __name__ == "__main__":
    main()