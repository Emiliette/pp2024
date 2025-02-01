# Copy your practical work 1 to 2.student.mark.oop.py
# Make it OOP’ed
# Same functions
# - Proper attributes and methods
# - Proper encapsulation
# - Proper polymorphism
# • e.g. .input(), .list() methods

class Class_Students: 
    def __init__(self):
        self.__id = input("Enter the student's ID: ")
        self.__name = input("Enter the student's Name: ")
        self.__dob = input("Enter the student's DoB: ")
        self.__mark = {}

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

    # Save marks of students for the specific course
    def set_mark(self, course_id, mark):
        self.__mark[course_id] = mark

    # Get marks of students for the specific course
    def get_mark(self, course_id):
        return self.__mark.get(course_id, None)
    
class Class_Courses:
    def __init__(self):
        self.__id = input("Enter the course's ID: ")
        self.__name = input("Enter the course's name: ")

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    
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
              8. Show marks for a given course""")
        
        option = int(input("Enter your choice: "))

        if option == 0:
            print("Exiting program. Goodbye!")
            break

        elif option == 1:
            university.set_num_students()

        elif option == 2:
            university.set_num_students()
            university.set_students()

        elif option == 3:
            university.set_num_courses()

        elif option == 4:
            university.set_num_courses()
            university.set_courses()

        elif option == 5:
            university.set_num_students()
            university.set_students()
            university.set_num_courses()
            university.set_courses()
            university.input_mark()

        elif option == 6:
            university.set_num_courses()
            university.set_courses()
            university.list_courses()

        elif option == 7: 
            university.set_num_students()
            university.set_students()
            university.list_students()

        elif option == 8:
            university.set_num_students()
            university.set_students()
            university.set_num_courses()
            university.set_courses()
            university.input_mark()
            university.show_mark()

if __name__ == "__main__":
    main()


