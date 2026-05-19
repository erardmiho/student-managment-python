from core import Student, Course, User
import json
class StudentManagmentSystem:
#add, remove students, add and remove courses, enrolling students in courses, view students enrolled courses and courses available
  def __init__(self):
    #Student object
    self.students = []
    # course object
    self.courses =[]
    self.next_student_id = 1
    self.next_course_id = 1
    self.enrollments = {}  # {student_id: [course_id, ...]}
    self.current_user = None
    self.users = {} #professor user
    #self.load_data("data.json")  # Load data from file on initialization

  def add_student(self, name, age, id, grade, enrollments):
    student = Student(name, age, id, grade, enrollments)
    self.students.append(student)
    self.next_student_id += 1
    self.save_data("data.json")  # Save data after adding a student
    print(f"Student {name} added with ID {id}.")
   

  def remove_student(self,id):
    for student in self.students:
      if student.ID == id:
        self.students.remove(student)
        print(f"Student with ID {id} removed.")
        self.save_data("data.json")  # Save data after removing a student
        return
    print(f"Student with ID {id} not found.")

  def add_course(self, course_name, course_id, instructor):
    course = Course(course_name, course_id, instructor)
    self.courses.append(course)
    self.next_course_id += 1
    self.save_data("data.json")  # Save data after adding a course
    print(f"Course {course_name} added with ID {course_id}.")
    

  def remove_course(self, course_id):
    for course in self.courses:
      if course.course_ID == course_id:
        self.courses.remove(course)
        self.save_data("data.json")  # Save data after removing a course
        print(f"Course with ID {course_id} removed.")
        return
    print(f"Course with ID {course_id} not found.")

  def enroll_student_in_courses(self, student_id, course_id):
    for student in self.students:
      if student.ID == student_id:
        for course in self.courses:
          if course.course_ID == course_id:
            if student_id not in self.enrollments:
              self.enrollments[student_id] = []
            self.enrollments[student_id].append(course_id)
            self.save_data("data.json")  # Save data after enrolling a student in a course
            print(f"Student with ID {student_id} enrolled in course with ID {course_id}.")
            return
        print(f"Course with ID {course_id} not found.")
        return
    print(f"Student with ID {student_id} not found.")

  def view_student_courses(self, student_id):
    if student_id in self.enrollments:
      course_ids = self.enrollments[student_id]
      courses = [course.course_name for course in self.courses if course.course_ID in course_ids]
      print(f"Student with ID {student_id} is enrolled in: {', '.join(courses)}")
      
    else:
      print(f"Student with ID {student_id} is not enrolled in any courses.")

  def view_available_courses(self):
    if self.courses:
      print("Available courses:")
      for course in self.courses:
        print(f"{course.course_name} (ID: {course.course_ID}, Instructor: {course.instructor})")
    else:
      print("No courses available.")

  ######################################################### log in and log out functionality

  def signup(self):
    print("\n --- Sign Up ---")
    username = input("Choose a username: ").strip()
    if username in self.users:
        print("Username exists. Try another one.")
        return False
    password = input("Choose a password: ").strip()
    self.users[username] = User(username, password)
    print(f"Account created for {username}. Log in.")
    self.save_data("data.json")
    return True

  def login(self):
    print("\n --- Log In ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = self.users.get(username)
    if user and user.password == password:
        self.current_user = user
        print(f"\n {user}")
        print("Login successful.\n")
        return True
    else:
        print("Invalid username or password. ")
        return False
    
  def logout(self):
    if self.current_user:
        print(f"\n{self.current_user.username} logged out.\n")
        self.current_user = None
    else:
        print("No user is currently logged in.")

######################################################### log in and log out functionality

########################################################## JSON WORK

  def save_data(self, filename):
    data = {
      "Student_ID": self.next_student_id,
      "Course_ID": self.next_course_id,
      "students": [vars(student) for student in self.students],
      "courses": [vars(course) for course in self.courses],
      "enrollments": self.enrollments,
      "users": {username: vars(user) for username, user in self.users.items()}
    }

    # also save enrollments inside courses
    for course in self.courses:
      course.enrollments = [student_id for student_id, course_ids in self.enrollments.items() if course.course_ID in course_ids]

    with open(filename, 'w') as f:
      json.dump(data, f)

  def load_data(self, filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)

        self.next_student_id = data.get("Student_ID", 1)
        self.next_course_id = data.get("Course_ID", 1)

        self.students = [Student(**student) for student in data.get("students", [])]
        self.courses = [Course(**course) for course in data.get("courses", [])]
        self.enrollments = data.get("enrollments", {})

        self.users = {
            username: User(**user)
            for username, user in data.get("users", {}).items()
        }

    except FileNotFoundError:
        print("No previous data found. Starting fresh.")

