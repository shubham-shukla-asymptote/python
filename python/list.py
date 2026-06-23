# l1=['lemon','ginger','mint','black','Oolong']
# print(len(l1))
# print(l1[2])
# ## you can use slicing 
# print(l1[1:3]) # same as string you can apply all methods from string 

# #if you want to      replace .('lemon','milk')  not allowed
# # l1[1:3]=[]   ## this is a delete operation 
# l1[1:3]=["milk"]  ## this is replace method right side l1[1:3] is a list and right side also we have to give a list if we give a string then it treat all the character as list 
# print(l1)
# l1[1:1]=["test","test"]   ## without deleting any element adding element 
# print(l1)


# ##append() add element at the last position 
# l1.append("ginger")
# print(l1)
# print(l1.pop()) ## it delete last element and give that last element as output 
# print(l1)
# l1.insert(1,"ginger")
# print(l1)
# l1.remove("ginger")
# print(l1)


# tea_varities=l1 ## same reference in memory 
# tea_varities=l1.copy() ##  different memory reference 
# tea_varities=['lemon','ginger','mint','black','Oolong'] ##  different memory reference 




## we can also use loop in list 
squared_num=[x**2  for x in range(10)] ## 10 not include in the range
print(squared_num)
print(range(10))

## del also used to delete elements del l1[" attribute"]