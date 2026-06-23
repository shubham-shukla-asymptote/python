#create a decortor to print the function name and value of its argument every time when function calls
def debug(func):
    def wrapper(*args,**kwargs):
        args_value=', '.join(str(arg)for arg in args)
        kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())
        print(f"calling:{func.__name__}  with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper
@debug
def hello():
    print("Hello! devil")
@debug    
def addNum(a,b):
    print(a+b)
    return a+b
hello()
addNum(8,7)