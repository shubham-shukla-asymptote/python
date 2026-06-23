import random
from decimal import Decimal
from fractions import Fraction
# # print(int(random.random()*10))    // it also print integer 
# print(random.randint(1,10)) # it also print integer 

# ################ we can also take choice for which we want to generate random choice  using random.choice()
# l1=['lemon','ginger','masala','mint']
# print(random.choice(l1))
# print(random.shuffle(l1))  ## shuffle method is used for the shuffle elment from list or collection



# ############# there are some problem in python with decimal precision 
# # a=0.1+0.1+0.1 
# # print(a) ## 0.30000000000000004 this is output but we know that output should be 0.3
# # a-=0.3
# # print(a)   ###5.551115123125783e-17 unexpected result comes  we know that ans must be zero but whhat the python doing here if we want to obtain out expected result then we have to import decimal
# a=Decimal('0.1')+Decimal('0.1')+Decimal('0.1') 
# print(Decimal(a))
# a-=Decimal('0.3')

# print(Decimal(a))
 #  we also Fraction which help us for fraction calculation
x=Fraction(2,7)+Fraction(7,2)
print(x)
print(Decimal('x'))