# Typecasting = The process of converting a variable from one DT to another
#               str(), int(), float(), bool()

name = "Mohit"
age = 20
gpa = 9.07
is_student = True



print(f"Type of GPA: {type(gpa)}")
gpa = int(gpa) #TypeCasted
print(f"After gpa TC: {type(gpa)}") #int
print(f"GPA after TC: {gpa}") # 9


print(f"Type of age: {type(age)}")
age = float(age)
print(f"Age after TC: {type(age)}")
print(f"Age after TC: {age}")


print(f"Type of name: {type(name)}")
name = bool(name)
print(f"Name after TC: {type(name)}")
print(f"Name after TC: {name}") 

