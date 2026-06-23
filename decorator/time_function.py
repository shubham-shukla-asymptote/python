import time
def timer(func):
    start=time.time()
    def wrapper(*args,**kwargs):
    
        result=func(*args,**kwargs)
        end=time.time()
        print((f"{func.__name__} took {end-start} to execute"))
        return result

    return wrapper  
    
@ timer
def example_timer(n):   #if we want to make tole of timer function the every function must pass from timer function then we use decorator @function_name
     time.sleep(n)

example_timer(2)


