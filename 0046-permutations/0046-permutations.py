def per(nums,s=None):
    c=[]
    if s is None:
        s=[]
    if not nums:
        c.append(s)
        return c
    for i in range(len(nums)):
        c += per(nums[:i]+nums[i+1:],s+[nums[i]])
    return c

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return per(nums)
        