from Online_Learning_Platform import *

def main():
    continue_asking = True
    while continue_asking:
        first_choice_for_user = int(input("Select 1 to log in as Instructor, 2 to log in as Administrator, 3 to log in as Student or 4 to Exit: "))
        match first_choice_for_user:
            case 1:
                instructor_choices = int(input("Select 1 to add Instructor, 2 to Update Instructor Details: "))
                if instructor_choices == 1:
                    age = int(input("Please input your age: "))
                    name = input("Please input your name: ")
                    email = input("Please input your email: ")
                    courses = input("Please input your courses: ")
                    instructor = Instructor(name,age,email,courses)
                    instructor.add_instructor_to_instructors_table()
                elif instructor_choices == 2:
                    Instructor.update_instructor_details()
            case 2:
                administrator_choices = int(input("Select 1 to Delete Student, 2 to Delete Instructor, 3 to See all Students, 4 to see all instructors: "))
                if administrator_choices == 1:
                    print("Here is the list of all students")
                    Student.read_data_from_student_table()
                    student_name = input("Type name of student to be deleted: ")
                    student_id = int(input("Type id of the student: "))
                    Student.delete_student_from_student_table(student_name,student_id)
                elif administrator_choices == 2:
                    print("Here is the list of all students")
                    Instructor.read_data_from_instructor_table()
                    instructor_name = input("Type name of instructor to be deleted: ")
                    instructor_id = int(input("Type id of the instructor: "))
                    Instructor.delete_instructor_from_instructor_table(instructor_name,instructor_id)
                elif administrator_choices == 3:
                    Student.read_data_from_student_table()
                elif administrator_choices == 4:
                    Instructor.read_data_from_instructor_table()
            case 3:
                student_choices = int(input("Select 1 to add Instructor, 2 to Update Instructor Details: "))
                if student_choices == 1:
                    studentage = int(input("Please input your age: "))
                    studentname = input("Please input your name: ")
                    studentemail = input("Please input your email: ")
                    studentcourses = input("Please input your courses: ")
                    student = Student(studentname,studentage,studentemail,studentcourses)
                    student.add_student_to_students_table()
                elif instructor_choices == 2:
                    Student.update_student_details()
            case 4:
                print("Goodbye")
                continue_asking = False
                os.system('cls')
            case _:
                print("Invalid Entry")












if __name__ == '__main__':
    main()