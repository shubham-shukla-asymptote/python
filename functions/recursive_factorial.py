def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)
    ## we have to focus on the base case and the recursive case to avoid infinite recursion and to ensure that the function eventually terminates. In this example, the base case is when n is 0, where we return 1, and the recursive case is when n is greater than 0, where we call the function itself with n - 1 until we reach the base case.