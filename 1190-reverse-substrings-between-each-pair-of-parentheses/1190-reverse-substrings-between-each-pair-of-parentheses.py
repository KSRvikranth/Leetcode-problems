class Solution:
    def reverseParentheses(self, s: str) -> str:
        a=[]
        s=list(s)
        for i in range(len(s)):
            if(s[i]=='('):
                a.append(i)
            if(s[i]==')'):
                b=a[-1]
                if(i-b!=1):
                    s[b+1:i]=reversed(s[b+1:i])
                a.pop()
        c=[]
        for i in range(len(s)):
            if(s[i].isalpha()):
                c.append(s[i])
        return "".join(c)
