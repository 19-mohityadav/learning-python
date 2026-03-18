# Class Variable --> shared among all instances of a class
#                    Defined outside the constructor
#                    Allow you to share data among all objects created from that class

# Instance variable --> defined inside the constructor


class Student:

    # Class Variable
    class_year = 2028
    num_students = 0


    def __init__(self, name, age):
        self.name = name  #instance Var
        self.age = age
        Student.num_students += 1

student1 = Student("Mohit", 20)
# print(student1.name)
# print(student1.age)
# print(student1.class_year)  #Bad access
print(Student.class_year)   #Good Access
print(Student.num_students)

student2 = Student("Rohit", 15)
print(Student.class_year)
print(Student.num_students)