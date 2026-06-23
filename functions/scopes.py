def scopes():
    x = 10  # This variable is in the local scope of the function
    print("Inside the function, x =", x)

scopes()

#local scopes are the variables that are defined inside a function and can only be accessed within that function. They are created when the function is called and destroyed when the function exits.
# global scopes are the variables that are defined outside of any function and can be accessed from anywhere in the code. They are created when the program starts and destroyed when the program ends.
# function scopes are same as local scopes
# other types of scopes include built-in scope, which contains built-in functions and variables that are always available in Python, and enclosing scope, which refers to the scope of any enclosing functions when dealing with nested functions. Understanding these scopes is crucial for managing variable visibility and avoiding naming conflicts in your code.




#example of other types of scopes
def outer_function():
    x = "Hello"  # This variable is in the enclosing scope of the inner function

    def inner_function():
        global x
        x="Hi"  
        
        # This variable is in the local scope of the inner function
        #avoid using global variables as much as possible because it can lead to code that is difficult to debug and maintain. Instead, it's often better to pass variables as parameters to functions or use return values to share data between functions, which helps to keep the code more modular and easier to understand.


        print("Inside the inner function, x =", x)  # Accessing the variable from the enclosing scope

    inner_function()


# return refernces to parent functions
outer_function() ## then we can access the variable x from the inner function which is in the enclosing scope of the outer function. when we call outer_function(), it will execute inner_function() and print the value of x, which is "Hi" because we have modified it using global keyword.




 #example in other function of returning reference to parent function
def parent_function():
    x = "Hello from parent function"

    def child_function():
        print(x)  # Accessing the variable from the parent function

    return child_function  # Returning a reference to the child function
result = parent_function()  # Calling the parent function to get the child function reference
result()  # Calling the child function, which will print the value of x from the parent function 
#the value of x is "Hello from parent function" because the child function has access to the variables in its enclosing scope, which includes the parent function's scope. When we call result(), it executes child_function(), which prints the value of x from the parent function.




def chai_coder(num):
    def pow(exponent):
        return num ** exponent
    return pow
result = chai_coder(2)  # This will return the pow function with num set to 2
print(result(3))  # This will call the pow function with exponent set to 3