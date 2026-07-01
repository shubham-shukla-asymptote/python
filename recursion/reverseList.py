def swapItem(l,r,list):
    if(l>=r):
        return 
    list[l],list[r]=list[r],list[l]
    swapItem(l+1,r-1,list)
list=[15,6,78,24,9,4,5]    
swapItem(0,len(list)-1,list)
print(list)
    