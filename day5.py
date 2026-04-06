
# #write a function to reverse the order of elements im list
# list=[1,2,3,4,5]
# print(list[::-1])




# #check the palindrome list
# list=[1,2,3,2,1]
# print(list)
# print(list[::-1])
# if list==list[::-1]:
#     print("palimdrome list")
# else:
#     print("not palindrome")





# #class

# class student:
#     roll_no = 101
    
#     def studentData(self):
#         print("student information")

# obj=student()
# print(obj.roll_no)
# obj.studentData()




# class demo:
#     def __init__(self):
#         print("i am constructor")

#     def msg(self):
#         print("hello class")

# obj1=demo()
# obj2=demo()
# obj1.msg()





# class Hod:
#     def __init__(self):
#         self.name = "sahil shirsat"
#         self.age = 53
#         self.empid = 1001

#     def info(self):
#         print("My name is:", self.name)
#         print("My age is", self.age)
#         print("My empid is", self.empid)

# obj = Hod()
# obj.info()



# class Hod:
#     def __init__(self, name, age, empid):
#         self.name = name
#         self.age = age
#         self.empid = empid

#     def info(self):
#         print("My name is:", self.name)
#         print("My age is", self.age)
#         print("My empid is", self.empid)

# obj = Hod('Arjun', 45, 101)
# obj.info()




# class New:
#     def __init__(self):
#         self.a = 10

# obj1 = New()
# obj2 = New()
# obj3 = New()

# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# obj1.a = 20

# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)






# #declaring instance variable outside the class by using object
# class Student:
#     def __init__(self):
#         self.s_name = "sahil"
#         self.s_rollno = "45"
        
#     def getdata(self):
#         self.s_mb = 282828228282

# # object creation (outside class)
# obj = Student()

# # adding instance variable using method
# obj.getdata()

# # deleting instance variable
# del obj.s_mb

# # adding instance variable outside class
# obj.s_branch = "CE"

# # printing all instance variables
# print(obj.__dict__)





# class New:
#     a=10
    
#     def __init__(self):
#         self.name = "sahil"
        
        

# obj1 = New()
# obj2 = New()
# obj3 = New()

# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

# New.a = 20

# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)







# import sys

# class CRUD:
#     def __init__(self):
#         print("Student Management System")
#         self.StudentId = []
#         self.StudentName = []
#         self.StudentRollNo = []
#         self.StudentCity = []

#     def addStudent(self):
#         self.StudentId.append(input("Enter student id: "))
#         self.StudentName.append(input("Enter student name: "))
#         self.StudentRollNo.append(input("Enter roll no: "))
#         self.StudentCity.append(input("Enter city: "))
#         print("Student added successfully!")
        
    

# # object
# obj = CRUD()
# obj.addStudent()

# print(obj.StudentId)
# print(obj.StudentName)
# print(obj.StudentRollNo)
# print(obj.StudentCity)




# class student:
#     def _init_(self,name,rollno,mob):
#         self.name = name
#         self.rollno = rollno
#         self.mob = mob

#     def display(self):
#         print(self.name," ",self.rollno," ", self.mob)

# stud = student("prashant",1001,646464646)
# stud.display()



#--------------------------------------------------------------------------------------------------------------------------------
# class Student:
#     @staticmethod
#     def get_personal_detail(first_name, last_name):
#         print("Your personal details:", first_name, last_name)
       
#     @staticmethod 
#     def contact_detail(mobile_no, roll_no):
#         print("Your contact details:", mobile_no, roll_no)
        
# Student.get_personal_detail("sahil", "shirsat")
# Student.contact_detail(1234567890, 101)


#--------------------------------------------------------------------------------------------------------------------------------

# class Collage:
#     def collage_name(self):
#         print("modern collage")
    
# class Student(Collage):
#     def student_info(self):
#         print("Name: sahil shirsat")
#         print("Branch:cse")
        
# obj=Student()
# obj.collage_name()
# obj.student_info()


#--------------------------------------------------------------------------------------------------------------------------------

# #multilevel inheritance
# class Collage:
#     def collage_name(self):
#         print("modern collage")
        
# class Student(Collage):
#     def student_info(self):
#         print("Name: sahil shirsat")
#         print("Branch:cse")
        
# class Exam(Student):
#     def subject(self):
#         print("subject1: python")
#         print("subject2: java")
#         print("subject3: c++")
        
# obj=Exam()
# obj.collage_name()
# obj.student_info()
# obj.subject()


#--------------------------------------------------------------------------------------------------------------------------------


# class SubjMarks:
#     math=int(input("Enter marks for math: "))
#     python=int(input("Enter marks for python: "))
#     java=int(input("Enter marks for java: "))
#     c=int(input("Enter marks for c: "))
    
# class PractMarks:
#     cpract=int(input("Enter marks for c practical: "))
    
# class Result(SubjMarks,PractMarks):
#     def total(self):
#         if self.math>=40 and self.python>=40 and self.java>=40 and self.c>=40 and self.cpract>=40:
#             print("You are eligible for admission")
#         else:
#             print("You are not eligible for admission")
        
# obj=Result()
# obj.total()

#--------------------------------------------------------------------------------------------------------------------------------


# # polymorphism
# class Principal:
#     def role(self):
#         print("I am managing all the activities")
        
# class Dean:
#     def role(self):
#         print("I am decision taking person")
        
# class HOD:
#     def role(self):
#         print("I am head of the department")
        
# class Faculty:
#     def role(self):
#         print("I am teaching the subject")
        
# def func(obj):
#     obj.role()

# campus = [Principal(), Dean(), HOD(), Faculty()]

# for obj in campus:
#     func(obj)
    
#--------------------------------------------------------------------------------------------------------------------------------

# #python doesn't function overloading

# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         else:
#             print("enter at least two numbers")
            
# obj=Arithmetic()
# obj.add(10)
# obj.add(1,2)
# obj.add(1,2,3)

#--------------------------------------------------------------------------------------------------------------------------------

# class Arithmetic:
#     def __init__(self):
#         print("There are no arguments")
        
#     def add(self, a):
#         print("There is only one argument:", a)
        
#     def sub(self, a, b):
#         print("There are two arguments:", a, b)
        
# obj = Arithmetic()
# obj.add(10)
# obj.sub(10, 20)

#--------------------------------------------------------------------------------------------------------------------------------

# class Rbi:
#     def home_loan(self):
#         print("home loan")
        
#     def car_loan(self):
#         print("car loan")
        
# class Sbi(Rbi):
#     def home_loan(self):
#         print("sbi home loan")
        
#     def car_loan(self):
#         print("sbi car loan")
        
# obj=Sbi()
# obj.home_loan()
# obj.car_loan()
#--------------------------------------------------------------------------------------------------------------------------------

# class Father:
#     def __init__(self):
#         print("Father = I am already at the breakfast table")
        
# class Child(Father):
#     def __init__(self):
#         print("Child = I will be late for breakfast")
#         super().__init__()
    
# obj = Child()
        
    