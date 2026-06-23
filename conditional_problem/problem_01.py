age=int(input("enter your age:"))
day=input("tell me the day:")
# price=0
# if age<18 and day=='wednesday':
#     price=6
# elif age>=18 and day=='wednesday':
#     price=10   
# elif age<18:
#     price=8
# else:
#     price=12   

# print(price)

price=12 if age>=18 else 8 
print(price)
price=price-2 if day=='wednesday' else price
print(price)