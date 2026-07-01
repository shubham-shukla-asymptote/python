def isPalindrome(str,i):
    n=len(str)
    if(i>=n/2):
        return True
    if str[i]!=str[n-i-1]:
        return False
    return isPalindrome(str,i+1)
 
print(isPalindrome("malayalam",0))
       