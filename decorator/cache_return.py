
import time
def cache_return(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            print("cache hit")
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper
@cache_return
def long_running_function(a,b):
    time.sleep(4)
    return a+b
print(long_running_function(4,5))
print(long_running_function(8,7))
print(long_running_function(1,2))



