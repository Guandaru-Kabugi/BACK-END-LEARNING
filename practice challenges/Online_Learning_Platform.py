import os
from dotenv import load_dotenv
import mysql.connector
import re

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def open_database_connection():
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD
        )
def execute_sql_commands(filename):
    mydatabase = open_database_connection()
    mycursor = mydatabase.cursor()
    with open(filename, 'r') as file:
        sql_commands = file.read().split(';')
        for command in sql_commands:
            if command.strip():
                mycursor.execute(command)
    mydatabase.commit()
    print('success')
    mycursor.close()
    mydatabase.close()
# execute_sql_commands('practice challenges\LMS.sql')

class Person:
    def __init__(self,name,age,email):
        self._name = name
        self._age = age
        self._email = email
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @property
    def email(self):
        return self._email
    @age.setter
    def age(self,value):
        if value<0:
            print("Age cannot be less than zero")
        else:
            self.age = value
    @staticmethod
    def validate_email(email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            return re.fullmatch(regex, email)
        else:
            print('invalid email.')
            
    def __repr__(self):
        return f"Name: {self.name} Age: {self.age} Email: {self.email}"

# person1 = Person('Alex',27,'kabugigu@gmail.com')
# print(person1)

class Instructor(Person):
    instructor_number_count = 0
    def __init__(self, name, age, email,*args):
        super().__init__(name, age, email)
        self._instructor_id = None
        self._course = list(args)
    @property
    def instructor_id(self):
        return self._instructor_id
    @property
    def courses(self):
        return self._course
    def remove_course(self):
        pass
    def add_course(self):
        pass
    def display_courses(self):
        pass
    @classmethod
    def instructor_count(cls):
        return Instructor.instructor_number_count
    def add_instructor_to_instructors_table(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Instructors WHERE InstructorName = %s AND InstructorEmail = %s'
        check_values = (self.name,self.email)
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_query,check_values)
        results = mycursor.fetchone()
        if results:
            print("Instructor details already exists")
        else:
            query = 'INSERT INTO Instructors(InstructorAge,InstructorName,InstructorEmail,Courses) VALUES(%s,%s,%s,%s)'
            courses_str = ','.join(self._course)
           
            values = (self.age,self.name,self.email,courses_str)
            mycursor.execute(query,values)
            mydatabase.commit()
            print("Instructor added successfully.")
            Instructor.instructor_number_count += 1
            mycursor.close()
            mydatabase.close()
    @classmethod
    def read_data_from_instructor_table(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Instructors'
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_query)
        results = mycursor.fetchall()
        for result in results:
            print({
                'Instructor ID': result[0],
                'Instructor Age': result[1],
                'Instructor Name':result[2],
                'Instructor Email':result[3],
                'Instructor Courses':list(result[4].split(','))})
        mycursor.close()
        mydatabase.close()
    @classmethod
    def update_instructor_details(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        mycursor.execute('USE LearningManagementSystem')
        choice = int(input("Select 1 to update Email and 2 to Update Courses:  "))
        if choice == 1:
            new_email = input("Provide New Email:  ")
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            if re.fullmatch(regex, new_email):
                id = int(input("Provide Your ID:  "))
                check_instructor = 'UPDATE Instructors SET InstructorEmail = %s WHERE InstructorID = %s'
                values = (new_email,id)
                
                mycursor.execute(check_instructor,values)
                mydatabase.commit()
                print("Successfully updated Email Address")
            else:
                print("invalid email address")
        elif choice == 2:
            id = int(input("Provide Your ID:  "))
            query= 'SELECT Courses From Instructors WHERE InstructorID = %s'
            values = (id, )
            mycursor.execute(query,values)
            results = mycursor.fetchone()
            if results:
                current_courses_by_instructor = results[0].split(',')
                print(f"Current Courses: {current_courses_by_instructor}")
                decision_user = int(input("Select 1 to add course or 2 to delete a course: "))
                if decision_user == 1:
                    new_unadded_course = input("Please type your new course:  ")
                    if not new_unadded_course in current_courses_by_instructor:
                        current_courses_by_instructor.append(new_unadded_course)
                    else:
                        print("Course Already in the list")
                elif decision_user == 2:
                    course_to_delete = input("Please type the course you want deleted:  ")
                    if course_to_delete in current_courses_by_instructor:
                        current_courses_by_instructor.remove(course_to_delete)
                    else:
                        print("The course is not available in the list")
                updated_new_courses = ','.join(current_courses_by_instructor)
                update_instructor_course = 'UPDATE Instructors SET Courses = %s WHERE InstructorID = %s'
                values = (updated_new_courses,id)
                mycursor.execute(update_instructor_course,values)
                mydatabase.commit()
                print("Successfully updated the courses")
                mycursor.close()
                mydatabase.close()    
    @classmethod
    def delete_instructor_from_instructor_table(cls,instructor_name,instructor_id):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_instructor = 'SELECT * FROM Instructors WHERE InstructorName = %s AND InstructorID = %s'
        value = (instructor_name, instructor_id)
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_instructor,value)
        results = mycursor.fetchone()
        if results:
            check_query = 'DELETE FROM Instructors WHERE InstructorName = %s AND InstructorID = %s'
            values = (instructor_name, instructor_id)
            mycursor.execute(check_query,values)
            mydatabase.commit()
            print(f"Successfully deleted {instructor_name} from the platform.")
        else:
            print("Name and ID Not Found")
        mycursor.close()
        mydatabase.close()
class Student(Person):
    student_number_count = 0
    def __init__(self, name, age, email,*args):
        super().__init__(name, age, email)
        self._student_id = None
        self._courses = list(args)
    @property
    def student_id(self):
        return self._student_id
    @property
    def courses(self):
        return self._courses
    @classmethod
    def student_count(cls):
        return cls.student_number_count
    def add_student_to_students_table(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Students WHERE StudentName = %s AND StudentEmail = %s'
        check_values = (self.name,self.email)
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_query,check_values)
        results = mycursor.fetchone()
        if results:
            print("Student details already exists")
        else:
            query = 'INSERT INTO Students(StudentAge,StudentName,StudentEmail,Courses) VALUES(%s,%s,%s,%s)'
            courses_str = ','.join(self._courses)
            values = (self.age,self.name,self.email,courses_str)
            mycursor.execute(query,values)
            mydatabase.commit()
            print("Student added successfully.")
            Student.student_number_count += 1
            mycursor.close()
            mydatabase.close()
    @classmethod
    def read_data_from_student_table(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Students'
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_query)
        results = mycursor.fetchall()
        for result in results:
            print({
                'Student ID': result[0],
                'Student Age': result[1],
                'Student Name':result[2],
                'Student Email':result[3]
            })
        mycursor.close()
        mydatabase.close()
    @classmethod
    def update_student_details(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        mycursor.execute('USE LearningManagementSystem')
        choice = int(input("Select 1 to update Email and 2 to Update Courses:  "))
        if choice == 1:
            new_email = input("Provide New Email:  ")
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            if re.fullmatch(regex, new_email):
                id = int(input("Provide Your ID:  "))
                check_query = 'UPDATE Students SET StudentEmail = %s WHERE StudentID = %s'
                student_values = (new_email,id)
                
                mycursor.execute(check_query,student_values)
                mydatabase.commit()
                print("Successfully updated Email Address")
            else:
                print("invalid email address")
        elif choice == 2:
            id = int(input("Provide Your ID:  "))
            student_query= 'SELECT Courses From Students WHERE StudentID = %s'
            values = (id, )
            mycursor.execute(student_query,values)
            results = mycursor.fetchone()
            if results:
                current_courses_by_student = results[0].split(',')
                print(f"Current Courses: {current_courses_by_student}")
                decision_user = int(input("Select 1 to add course or 2 to delete a course: "))
                if decision_user == 1:
                    new_unadded_course = input("Please type your new course:  ")
                    if not new_unadded_course in current_courses_by_student:
                        current_courses_by_student.append(new_unadded_course)
                    else:
                        print("Course Already in the list")
                elif decision_user == 2:
                    course_to_delete = input("Please type the course you want deleted:  ")
                    if course_to_delete in current_courses_by_student:
                        current_courses_by_student.remove(course_to_delete)
                    else:
                        print("The course is not available in the list")
                updated_new_courses = ','.join(current_courses_by_student)
                update_student_course = 'UPDATE Students SET Courses = %s WHERE StudentID = %s'
                values = (updated_new_courses,id)
                mycursor.execute(update_student_course,values)
                mydatabase.commit()
                print("Successfully updated the courses")
                mycursor.close()
                mydatabase.close()    
    @classmethod
    def delete_student_from_student_table(cls,student_name,student_id):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_student = 'SELECT * FROM Students WHERE StudentName = %s AND StudentID = %s'
        value = (student_name, student_id)
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_student,value)
        results = mycursor.fetchone()
        if results:
            check_query = 'DELETE FROM Students WHERE StudentName = %s AND StudentID = %s'
            values = (student_name, student_id)
            mycursor.execute(check_query,values)
            mydatabase.commit()
            print(f"Successfully deleted {student_name} from the platform.")
        else:
            print("Name and ID Not Found")
        mycursor.close()
        mydatabase.close()
class Course:
    course_number_count = 0
    def __init__(self,course_name, *args):
        self._course_id = None
        self._course_name = course_name
        self._instructor_object = list(args)
        
    @property
    def course_id(self):
        return self._course_id
    @property
    def course_name(self):
        return self._course_name
    @property
    def instructor_object(self):
        return self._instructor_object
    @classmethod
    def get_course_count(cls):
        return cls.course_number_count
    @classmethod
    def course_count(cls):
        return cls.course_count
    def add_course_into_courses_table(self):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Courses WHERE CourseName = %s'
        check_values = (self.course_name, )
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_query,check_values)
        results = mycursor.fetchone()
        if results:
            print("Course name already in the database")
        else:
            query = 'INSERT INTO Courses(CourseName,CourseInstructor) VALUES(%s,%s)'
            instructor_names = [instructor.name for instructor in self._instructor_object]
            instructor_str = ','.join(instructor_names)
            values = (self.course_name,instructor_str)
            mycursor.execute(query,values)
            mydatabase.commit()
            print("Successfully added new course")
            Course.course_number_count+=1
            mycursor.close()
            mydatabase.close()
    @classmethod
    def read_data_from_courses_table(cls):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_query = 'SELECT * FROM Courses'
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_query)
        results = mycursor.fetchall()
        for result in results:
            print({
                'Course ID': result[0],
                'Course Name': result[1],
                'Course Instructor':list(result[2].split(','))
            })
        mycursor.close()
        mydatabase.close()
    @classmethod
    def delete_course_from_courses_table(cls,course):
        mydatabase = open_database_connection()
        mycursor = mydatabase.cursor()
        check_course = 'SELECT * FROM Courses WHERE CourseName = %s'
        value = (course, )
        mycursor.execute('USE LearningManagementSystem')
        mycursor.execute(check_course,value)
        results = mycursor.fetchone()
        if results:
            check_query = 'DELETE FROM Courses WHERE CourseName = %s'
            values = (course, )
            mycursor.execute(check_query,values)
            mydatabase.commit()
            print(f"Successfully deleted {course} course.")
        else:
            print("Course Not Found")
        mycursor.close()
        mydatabase.close()
        
    def __repr__(self):
        return f"Course ID: {self.course_id} Course Name: {self.course_name} Course Instructor: {self.instructor_object.name}"