def printName(name,n):
    if n<=0: return
    print(name)
    printName(name, n-1)


# printName("shubham",5)
def printN(i,n):
    if(i>n):
        return
    printN(i+1,n)
    print(i)
printN(1,10)      # in reverse order