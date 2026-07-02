m=[1,4,5,2];
n=len(m)
ans=[]
def  printSubsequences(i,  ans):
    if(i>=n):
        print(ans)
        return
    ans.append(m[i])
    printSubsequences(i+1,ans)
    ans.pop()
    printSubsequences(i+1,ans)

printSubsequences(0,ans)    

   
    