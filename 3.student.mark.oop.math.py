class Student:
    def __init__(self):
        self.__id = input("Enter the student's id: ")
        self.__name = input("Enter the student's name: ")
        self.__dob = input("Enter the student's dob: ")

    # Encapsulation part
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

class Course:
    def __init__(self):
        self.__id = input("Enter the course's id: ")
        self.__name = input("Enter the course's name: ")
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

class Utils:
    # Ask the user to input something
    def input_something(args):
        while True:
            try:
                value = int(input(f"Enter the number of {args}: "))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Show the list
    @staticmethod
    def show(items):
        if not items:
            print("No items available.")
            return
        for i, item in enumerate(items):
            print(f"{i + 1}. {item.get_id()} - {item.get_name()}")

class University:
    def __init__(self):
        # Initialize the list for DATA option
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
        std_numb = self.get_num_students()
        self.__num_students = Utils.input_something("students")            # Example of polyphomism

    def set_num_courses(self):
        crs_numb = self.get_num_courses()
        self.__num_courses = Utils.input_something("courses")              # Example of polyphomism

    def set_students(self):
        for _ in range(self.__num_students):
            self.__students.append(Student())

    def set_courses(self):
        for _ in range(self.__num_courses):
            self.__courses.append(Course())

    # Display a list of students
    def list_students(self):
        if not self.__students:
            print("No students available.")
            return
        print("Student list:")
        Utils.show(self.__students)

    # Display a list of courses
    def list_courses(self):
        if not self.__courses:
            print("No courses available.")
            return
        print("Course list:")
        Utils.show(self.__courses)

# Main function for the "game"
def main():
    univ = University()

    while True:
        print("""
    Options:
    0. Exit
    1. Input number of students
    2. Input number of courses
    3. Input student details
    4. Input course details
    5. List students
    6. List courses
    """) 
        option = int(input("Your choice: "))
        if option == 0:
            break

        elif option == 1:
            univ.set_num_students()
        elif option == 2:
            univ.set_num_courses()
        elif option == 3:
            univ.set_students()
        elif option == 4:
            univ.set_courses()
        elif option == 5:
            univ.list_students()
        elif option == 6:
            univ.list_courses()
        else:
            print("Invalid input. Please try again!")

# Call the main function
if __name__ == "__main__":
    main()