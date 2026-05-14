class Person:
  def __init__(self, name, age, ID):
    self.name = name
    self.age = age
    self.ID = ID

class Student(Person):
  def __init__(self, name, age, ID, grade, enrollments):
    super().__init__(name, age, ID)
    self.grade = grade
    self.enrollments = enrollments

  def __str__(self):
    return f"Student(Name: {self.name}, Age: {self.age}, ID: {self.ID}, Grade: {self.grade}, Enrollments: {self.enrollments})"

class Course:
  def __init__(self, course_name, course_ID, instructor):
    self.course_name = course_name
    self.course_ID = course_ID
    self.instructor = instructor

  def __str__(self):
    return f"Course(Name: {self.course_name}, ID: {self.course_ID}, Instructor: {self.instructor})"
  

class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

  def __str__(self):
    return f"User logged in as: {self.username}"