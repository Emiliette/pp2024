# Practical work 1: student mark management
# Functions
# - Input functions:
    # • Input number of students in a class
    # • Input student information: id, name, DoB
    # • Input number of courses
    # • Input course information: id, name
    # • Select a course, input marks for student in this course
# - Listing functions:
    # • List courses
    # • List students
    # • Show student marks for a given course

def input_no_students():
    no_students = int(input("Enter number of students: "))
    return no_students

def input_students_info():
    students = []
    no_students = input_no_students()

    for i in range(no_students):
        student_id = input(f"Enter student ID {i+1}: ")
        student_name = input(f"Enter student name {i+1}: ")
        student_dob = input(f"Enter student dob {i+1}: ")
        students.append({"ID": student_id, "Name": student_name, "DoB": student_dob, "marks": {}})

    return students

def input_no_courses():
    no_courses = int(input("Enter number of courses: "))
    return no_courses

def input_courses_info():
    courses = []
    no_courses = input_no_courses()

    for i in range(no_courses):
        course_id = input(f"Enter course ID {i+1}: ")
        course_name = input(f"Enter course name {i+1}: ")
        courses.append({"ID": course_id, "Name": course_name})

    return courses

def input_mark(students, courses):
    course_id = input("Enter the course ID to input marks: ")

    if not any(a['ID'] == course_id for a in courses):
        print("Invalid course ID.") 
    
    # Dòng 48 và 77, dùng in hay == đều như nhau
    
    for student in students:
        mark = float(input(f"Enter the mark for {student['Name']} - ID: {student['ID']}: "))
        student['marks'][course_id] = mark

def list_courses(courses):
    if len(courses) == 0:
        print("The list of courses is empty.")
    
    for course in courses:
        print(f"ID: {course['ID']}, Name: {course['Name']}")

def list_students(students):
    if len(students) == 0:
        print("The list of students is empty.")

    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, DoB: {student['DoB']}")

def show_marks(students):
    course_id = input("Enter the course ID you want to show: ")
    if not any(course_id in student['marks'] for student in students):
        print("Invalid course ID.")
        return

    # Dòng 48 và 77, dùng in hay == đều như nhau

    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, Marks: {student['marks']}")


# a = input_students_info()
# b = input_courses_info()
# input_mark(a,b)
# list_courses(b)
# list_students(a)
# show_marks(a)

def main():
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
            input_no_students()

        elif option == 2:
            input_students_info()
        
        elif option == 3:
            input_no_courses()
        
        elif option == 4:
            input_courses_info()
        
        elif option == 5:
            a = input_students_info()
            b = input_courses_info()
            input_mark(a, b)

        elif option == 6:
            b = input_courses_info()
            list_courses(b)

        elif option == 7:
            a = input_students_info()
            list_students(a)    

        elif option == 8:
            a = input_students_info()
            show_marks(a)

        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()