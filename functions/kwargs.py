def kw_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")  
        
        
        
        # kwargs is a dictionary of keyword arguments passed to the function.we can iterate through it using items() to access both keys and values.or we can access specific values using their keys, like kwargs['key_name'].this allows us to handle a variable number of keyword arguments in a flexible way.It is commonly used when we want to allow users to pass a varying number of named arguments to a function without having to define them all explicitly in the function signature.kwargs returns a dictionary of keyword arguments passed to the function, allowing us to access and manipulate them as needed. f" means we are using an f-string to format the output, where {key} and {value} will be replaced with the actual key and value from the kwargs dictionary when printed. This provides a convenient way to display the keyword arguments in a readable format.

        
kw_args(name="Alice", age=30, city="New York")
