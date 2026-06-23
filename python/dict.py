dict={'lemon':'spicy','ginger':'zesty','mint':'mild'}
# print(dict)
# for chai in dict:
#     print(chai)   ## only keys printed
# for chai in dict:
#     print(chai,dict[chai])    ### print both the value and the key 
#  ## we can also use both parameter in for loop with some modification in syntax
# for key,value in dict.items():
#     print(key,value)
# we can add key value pairs using dict["key"]=value  and pop ("key") and if we use popitem() no parameter to pass in the method 
## 2d dict
chai_shop={
    'chai':{'masala':'spicy','lemon':'normal'},
    'tea':{'ginger':'zesty','black':'strong'}
}
# print(chai_shop.keys())
# print(chai_shop['chai'].keys())
# print(chai_shop['chai'].values())
# print(chai_shop['chai']['lemon'])


##for loop in dictionary 
squared_num={x:x**2 for x in range(10)}
print(squared_num)

 ## clear() used to delete all the element 


 ## creating dictionary from a key list and a default value 
keys=['ginger','lemon','masala']
default_value='delicius'
new_dict=dict.fromkeys(keys,default_value) 
print(new_dict) ##{'ginger': 'delicius', 'lemon': 'delicius', 'masala': 'delicius'}
new_dict=dict.fromkeys(keys,keys) 
print(new_dict) ##{'ginger': ['ginger', 'lemon', 'masala'], 'lemon': ['ginger', 'lemon', 'masala'], 'masala': ['ginger', 'lemon', 'masala']}
