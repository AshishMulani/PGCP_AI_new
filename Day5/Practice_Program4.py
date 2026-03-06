#Q1 create class 'student' with rollno,studentname,dict/list of marks(subjectname-marks[3])
#a)initializer (__init__)
#a)implement __str__ method
#a)print student data for given id
#a)calculate GPA()
# gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3
class Student:
    def __init__(self,rollno,studentName,sub):
        self._rollno=rollno
        self._studentName=studentName
        self._sub=sub

    def __str__ (self):
        data=(f'StudentData: [Rollno: {self._rollno},Name:{self._studentName},Marks:{self._sub}]')
        return data


    def calculate_gpa(self):
        marks=self._sub['maths']
        gpa=(1/3)*marks[0]+(1/2)*marks[1]+(1/4)*marks[2]
        return gpa

#Q2 Create 5 student objects and store them in a list
# For the student data stored in the list perform following operation:
# 1. Display All Student

student=[Student(7,'Ashish',{'maths':[45,42,39]}),
Student(8,'Dhriti',{'maths':[40,48,47]}),
Student(9,'Pratiksha',{'maths':[44,43,39]}),
Student(4,'Vijay',{'maths':[41,45,37]}),
Student(6,'Pranita',{'maths':[45,42,39]})]

for i in student:
    print(i)
print('-------------------------------------------------------------------')
# 2. Search by id
# 4. Calculate GPA of a student
id=int(input('enter the id:'))
op=[i for i in student if i._rollno==8]

for i in op:
    print(i._studentName)
    print('GPA', i.calculate_gpa())

print('-------------------------------------------------------------------')

# 3. Sort by name
by_name=sorted(student,key=lambda s:s._studentName)
for i in by_name:
    print(i)



