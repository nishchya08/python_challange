# class variables = shared among all instances of a class
#                    Defined outside the constructor
#                    Allow you to share data among all objects created from that class

class student():

    class_year = 2025
    num_student =0
    def __init__(self, name,age):
        self.name = name
        self.age = age
        student.num_student += 1


student1= student('John',20)
student2 = student("Patrick",10)
student3 = student("Pattrick",10)

#print(student1.name,student1.age)
#print(student2.name,student2.age)
#print(student2.class_year)
#print(student.num_student)
print(f"My graduating of class {student.class_year} has {student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
