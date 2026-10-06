class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=[]
        c=0
        for i in range(len(s)):
            if(s[i]=='('):
                a.append(s[i])
            elif(s[i]==')' and len(a)>0):
                a.pop()
            else:
                c+=1
        return (len(a)+c)