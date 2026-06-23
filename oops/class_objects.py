# class student:
#     name = "Shubham"
#     age = 20
#     #constructor is a special method in a class that is automatically called when an object of the class is created.
    

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")
# # class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# # object is an instance of a class. It is created using the class as a template and can have its own unique values for the attributes defined in the class.
# student1 = student()  # creating an object of the student class
# student1.display()  # calling the display method of the student object





#  accses modifiers are used to control the access to the attributes and methods of a class. In Python, we have three types of access modifiers: public, protected, and private. Public attributes and methods can be accessed from anywhere, protected attributes and methods can be accessed within the class and its subclasses, and private attributes and methods can only be accessed within the class itself. In Python, we use a single underscore (_) to indicate that an attribute or method is protected, and a double underscore (__) to indicate that it is private. However, it's important to note that these are just conventions in Python and do not enforce strict access control like in some other programming languages.   


class student:
    count=0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1

    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}")
# student2=student("Alice", 25)        
# student2.display()