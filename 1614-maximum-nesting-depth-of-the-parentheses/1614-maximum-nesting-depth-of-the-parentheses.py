class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        a=[]
        m=0
        for i in range(len(s)):
            if(s[i]=='('):
                c+=1 
                a.append(i)
            elif(s[i]==')'):
                c-=1 
                a.pop()
            m=max(m,c)
        return m
            
