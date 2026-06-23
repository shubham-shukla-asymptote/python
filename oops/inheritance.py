from class_objects import student 
##inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes. The child class can also override or extend the functionality of the parent class by defining





class topper(student):
    def __init__(self,name,age,markspercentage):
        super().__init__(name,age) #super() is a built-in function in Python that allows you to call methods from a parent class. In this case, we are using super() to call the __init__ method of the student class, which initializes the name and age attributes for the topper class. This way, we can reuse the initialization logic defined in the student class while also adding additional attributes specific to the topper class, such as markspercentage.
        self.markspercentage=markspercentage
    def display(self):
        super().display() #super() is used here to call the display method of the parent class (student) to print the name and age attributes. After that, we can add additional functionality to display the markspercentage attribute specific to the topper class.
        print(f"Marks Percentage: {self.markspercentage}%")    

toper =topper("Shubham", 20, 95)
toper.display()
topperMaths=topper("Alice", 25, 90)
topperMaths.display()
print(isinstance(toper, topper))  # True
print(isinstance(toper, student))  # True



# we have to find number of instances of the student created
print(student.count)
