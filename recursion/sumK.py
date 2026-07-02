def sumK( target, i,list ,ansList,sum):
    l=len(list)
    
    if( i==l):
        if sum==target:
            print(ansList)
            return True
        else:
            return False    
    ansList.append(list[i])
    sum+=list[i]
    if (sumK(target,i+1,list,ansList,sum)==True):
        return True

    ansList.pop()
    sum-=list[i]
    if(sumK(target,i+1,list,ansList,sum)==True):
        return True
    return False    
list=[2,4,6,3,5,1,8]
ansList=[]
sum=0

sumK(8,0,list,ansList,sum)    

