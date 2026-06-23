##a lambda function is a small, anonymous function (i.e., without a name) that can have any number of arguments but only one expression.
##It is often used for short, throwaway functions where using def would be overkill.
cube=lambda x:x**3
print(cube(3)) ## calling a lambda function
newVar=cube   ## same reference 
print(newVar(3))