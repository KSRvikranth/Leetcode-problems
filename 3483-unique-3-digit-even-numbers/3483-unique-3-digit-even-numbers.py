class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s=set()
        def count(a,used):
            if(len(a)==3):
                if(a[0]!=0 and a[2]%2==0):
                    num=a[0]*100+a[1]*10+a[2]
                    s.add(num)
                return 
            for i in range(len(digits)):
                if i not in used:
                    used.add(i)
                    a.append(digits[i])
                    count(a,used)
                    a.pop()
                    used.remove(i)
        a=[]
        used=set()
        count(a,used)
        return len(s)
        