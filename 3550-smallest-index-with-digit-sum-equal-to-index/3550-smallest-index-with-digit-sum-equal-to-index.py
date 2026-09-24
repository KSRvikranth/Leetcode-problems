class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a=nums[i]
            s=0
            while(a>0):
                s+=a%10
                a//=10
            if(s==i):
                return i
        return -1