class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        a=[]
        while(nums):
            s=sorted(set(nums))
            
            for j in s:
                a.append(j)
                nums.remove(j)
        return a
                
                
            
            
                
            
            