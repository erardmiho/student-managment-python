from core import Student, Course, User
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

  def add_student(self, name, age, id, grade, enrollments):
    student = Student(name, age, id, grade, enrollments)
    self.students.append(student)
    self.next_student_id += 1
    print(f"Student {name} added with ID {id}.")

  def remove_student(self,id):
    for student in self.students:
      if student.ID == id:
        self.students.remove(student)
        print(f"Student with ID {id} removed.")
        return
    print(f"Student with ID {id} not found.")

  def add_course(self, course_name, course_id, instructor):
    course = Course(course_name, course_id, instructor)
    self.courses.append(course)
    self.next_course_id += 1
    print(f"Course {course_name} added with ID {course_id}.")

  def remove_course(self, course_id):
    for course in self.courses:
      if course.course_ID == course_id:
        self.courses.remove(course)
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
    
  def logut(self):
    if self.current_user:
        print(f"\n{self.current_user.username} logged out.\n")
        self.current_user = None
    else:
        print("No user is currently logged in.")

######################################################### log in and log out functionality