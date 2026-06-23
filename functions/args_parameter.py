def sum_all(*args):
    return sum(args) ##args is the tuple of parameter we can manipulate it 
print(sum_all(1,2))
print(sum_all(1,2,3,4,5,6))




##In Python, *args is a special syntax used in function definitions to allow a function to accept a variable number of positional arguments. These arguments are collected into a tuple, enabling flexible function calls without knowing the exact number of inputs in advance.or example, if you define a function like def my_function(*args):, you can call it with any number of arguments, and they will be accessible as a tuple named args within the function. This is particularly useful when you want to create functions that can handle an arbitrary number of inputs without having to specify each one explicitly in the function signature.




