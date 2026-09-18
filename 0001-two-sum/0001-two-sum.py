class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=sorted(nums)
        l=0
        r=len(a)-1
        b=[]
        while(l<=r):
            if(a[l]+a[r]==target):
                b.append(a[l])
                b.append(a[r])
                break
            elif(a[l]+a[r]>target):
                r-=1
            else:
                l+=1
        c=[]
        for i in range(len(nums)):
            if(nums[i] in b):
                c.append(i)
        return c


