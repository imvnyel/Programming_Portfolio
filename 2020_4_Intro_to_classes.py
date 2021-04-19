'''This exercise is an introduction to creating, accessing, and modifying Class instances.
This included practices such as creating Methods, checking Class attributes, and using Dunders
 Created on 06/04/2020 by Emmanuel Kaunda'''


from datetime import datetime
student_attendance = {}

class Student:
  date = datetime.now()
  fixed_date = date.strftime('%x')
  def __init__(self, name, year, attendance):
    self.name = name
    self.year = year
    self.grades = [100, 50, 50, 100]
    if attendance == 'y':
      self.is_here = True
    elif attendance == 'n':
      self.is_here = False
    else:
      'Incorrect format, please retry'
    self.attendance_dict = {self.fixed_date: self.is_here}
    print(self.attendance_dict)
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      return
  def get_average(self):
    avg = sum(self.grades)/len(self.grades)
    return print('Your average grade is {avg}'.format(avg=avg))

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def is_passing(self):
    if self.score > self.minimum_passing:
      print('Currently passing this class with a grade of {grade}'.format(grade=self.score))
    else:
      print('You are currently failing this class with a grade of {grade}'.format(grade=self.score))
    


roger = Student('Roger van der Weyden', 10, 'y')
sandro = Student('Sandro Botticelli', 12, 'y')
pieter = Student('Pieter Bruegel the Elder', 8, 'n')

pieter_grade = Grade(58)

pieter_grade.is_passing()
pieter.get_average()

student_attendance[roger.name] = [roger.attendance_dict]
student_attendance[sandro.name] = [sandro.attendance_dict]
student_attendance[pieter.name] = [pieter.attendance_dict]

for k in student_attendance:
  print(k, student_attendance[k])