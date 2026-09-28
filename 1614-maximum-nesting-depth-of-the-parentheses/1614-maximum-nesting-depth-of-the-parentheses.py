class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        m=0
        for i in range(len(s)):
            if(s[i]=='('):
                c+=1 
            elif(s[i]==')'):
                c-=1 
            m=max(m,c)
        return m
            
