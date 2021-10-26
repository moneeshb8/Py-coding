class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        re_n = 0
        
        if(x<0):
            return False
        else:
            num=x
            while num!=0:
               digit=num%10
               re_n=re_n*10+digit
               num//=10
                
        if(re_n==x):
            return True
        else:
            return False
