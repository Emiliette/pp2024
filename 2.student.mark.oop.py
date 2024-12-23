# Ask the user to input a number of unit (course / student)
def input_numStudents():
    return int(input(f"Enter the number of students in this class: "))

# Ask the user to enter a list of info for an type
def input_infos():

    # TODO: input info for the type (student/course info)

    students = []
    num_Studenets = input_numStudents()
   
    for i in range(num_Studenets):
        student_id = input(f"Enter ID for student {i + 1}: ")
        student_name = input(f"Enter name for student {i + 1}: ")
        student_dob = input(f"Enter date of birth (dd/mm/yyyy) for student {i + 1}: ")
        students.append({'id': student_id, 'name': student_name, 'dob': student_dob, 'marks': {}})
    
    return students

# Input the student mark in a course base on the course id
def input_mark(students, courses):

    # TODO: check mark in student or not
    # If not, enter the mark for the course

    course_id = input("Enter the course ID to input marks: ")
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} (ID: {student['id']}): "))
        student["marks"][course_id] = mark

# Display a list of students
def list_students(students):

    # TODO: check what happens if there's no student (hint: len(students))
    
    if len(students) == 0:  # Check if there are no students
        print("There aren't any students yet.")
        return

    # TODO: display the student list
    
    print("Here is the student list: ")

    # TODO: add loop function to check the info of student
    
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")
        if student["marks"]:
            print("   Marks:")
            for course_id, mark in student["marks"].items():
                print(f"     {course_id}: {mark}")

    # print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")

    # TODO: check if mark student and print out the information
    # if "marks" in student:
    #     print("Marks (Course Id - Mark): ", end="")   

# Display a list of courses
def list_courses(courses):
   
    # TODO: check what happens if there's no course (hint: len(course))
    
    if len(students) == 0:
        print("There aren't any courses yet")
        return
        
    print("Here is the course list: ")
    
    # TODO: add loop function to check the info of course
    
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")
    
    # print(f"{i+1}. {course['id']} - {course['name']}")

# Main function for the "game"
def main():
    # Initialize the list for DATA option
    courses = []
    students = []
    num_students = 0
    num_courses = 0

    while True:
        print("""
Options:
0. Exit
1. Input Students
2. Input Courses
3. Input Marks
4. List Students
5. List Courses
""")
        
        option = int(input("Enter your choice: "))

        if option == 0:
            print("Exiting program. Goodbye!")
            break

        elif option == 1:
            students = input_infos()

        elif option == 2:
            num_courses = int(input("Enter the number of courses: "))
            for i in range(num_courses):
                course_id = input(f"Enter ID for course {i + 1}: ")
                name = input(f"Enter name for course {i + 1}: ")
                courses.append({"id": course_id, "name": name})

        elif option == 3:
            input_mark(students, courses)

        elif option == 4:
            list_students(students)

        elif option == 5:
            list_courses(courses)
        
        else:
            print("Invalid input. Please try again!")

# Call the main function
if __name__ == "__main__":
    main()