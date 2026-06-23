def even_generator(n):
    for i in range(2, n+1, 2):
        ##return i 
        # ## problem with return is it will stop the function after first iteration and it will not give us all the even number up to n
        ## to solve this problem we can use yield instead of return
        yield i 
        ##yield will return the value of i and it will not stop the function it will continue to execute the next iteration until it reaches the end of the function or it encounters a return statement. this way we can get all the even number up to n when we iterate over the generator.
            
            
print(tuple(even_generator(10)))            
            ##yield is used to create a generator function that can be iterated over, allowing you to generate values on-the-fly without storing them all in memory at once. In this case, the even_generator function will yield even numbers up to n when iterated over.