

from managment_system import StudentManagmentSystem


def main_menu():
    print("\n" + "=" * 50)
    print("        WELCOME TO Student management system")
    print("=" * 50)
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")

def student_management():
    print("\n" + "=" * 50)
    print("        WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. Remove Student")
    print("3. List Students")
    print("4. Add Course")
    print("5. Remove Course")
    print("6. List Courses")
    print("7. Enroll Student in Course")
    print("8. View Student in specific Courses")
    print("9. Exit")

def main():
    system = StudentManagmentSystem()
    while True:
        main_menu()
        choice = input("Select an option: ")
        if choice == '1':
            system.signup()
        elif choice == '2':
            system.login()
            if system.current_user:
                while True:
                    student_management()
                    sm_choice = input("Select an option: ")
                    if sm_choice == '1':
                        name = input("Enter student name: ")
                        age = int(input("Enter student age: "))
                        grade = input("Enter student grade: ")
                        system.add_student(name, age, system.next_student_id, grade, [])
                    elif sm_choice == '2':
                        id = int(input("Enter student ID to remove: "))
                        system.remove_student(id)
                    elif sm_choice == '3':
                        for student in system.students:
                            print(student)
                    elif sm_choice == '4':
                        course_name = input("Enter course name: ")
                        instructor = input("Enter instructor name: ")
                        system.add_course(course_name, system.next_course_id, instructor)
                    elif sm_choice == '5':
                        course_id = int(input("Enter course ID to remove: "))
                        system.remove_course(course_id)
                    elif sm_choice == '6':
                        for course in system.courses:
                            print(course)
                    elif sm_choice == '7':
                        for student in system.students:
                            print(student)
                        student_id = int(input("Enter student ID you want to enroll: "))
                        course_id = int(input("Enter course ID you want to enroll the student in: "))
                        system.enroll_student_in_courses(student_id, course_id)
                    elif sm_choice == '8':
                        for student in system.students:
                            print(student)
                        student_id = int(input("Enter student ID: "))
                        system.view_student_courses(student_id)
                    elif sm_choice == '9':
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()