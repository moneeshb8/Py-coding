class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1: return False
        stack = []
        open_ = ['(', '{', '[']
        close_ = [')', '}', ']']
        
        for i in s:
            if(i in open_):
                stack.append(close_[open_.index(i)])
            elif(len(stack)!=0 and i==stack[-1]):
                stack.pop()
            else:
                return False
        return len(stack)==0
