import string
# chai='lemon tea'
# chai_first=chai[0]
# slice_chai=chai[0:5]  # last element is excluded 
# print(slice_chai)
# slice_chai2=chai[0:5:2]  ## third arguments tells us about hopping how many charcter you want to jump
# print(slice_chai2)
# reverse_chai=chai[::-1]  ## if we want to reverse the string 
# print(reverse_chai)
# chai2='    masala   tea    '   ### if we want to  delete  the extra space from starting and ending we can stripping 
# strip_chai=chai2.strip()
# print(strip_chai)
# print(chai.split()) ## give a list of charcter which are seperated with space 
# print("-".join(["A", "B", "C"]))    # A-B-C
#  ### other methods also like replace(),endswith,startwith etc





######### import string method
# print(string.ascii_letters)  # abc...XYZ
# print(string.digits)         # 0123456789
# print(string.punctuation)  

### one more method find either char or word
### count(" ") use to count the repetition of word 





################## one more important property used in python programming variable inserting in a string using {} in string and used order.format(variable....) 

# chai='masala tea'
# quantity=2
# order="I ordered {} cups of {} "
# print(order)
# print(order.format(quantity,chai))


#######handling unicode character  
chai_Compliment=" he said, \" masala tea is awesome\""  ## below line give string unterminated 
# handling_path=r"c:\same\pwd\"
handling_path="c:\\same\\name\\pwd\\"    # correct handling of path
print(handling_path)  



