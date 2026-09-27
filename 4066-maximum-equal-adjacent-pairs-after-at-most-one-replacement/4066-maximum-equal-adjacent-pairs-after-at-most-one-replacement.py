class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        an=0
        d={}
        for i in range(len(nums)-1):
            a=nums[i]
            b=nums[i+1]
            if(a==b):
                an+=1
            else:
                if(a>b):
                    a,b=b,a
                if a not in d:
                    d[a]={}
                if(b not in d[a]):
                    d[a][b]=0
                d[a][b]+=1 
        m=0
        for a in d:
            for b in d[a]:
                if(d[a][b]>m):
                    m=d[a][b]
        return an+m