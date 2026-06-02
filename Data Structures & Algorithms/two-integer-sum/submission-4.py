class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #arrays check all the elements.
        l=[]
        sum=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    return [i,j]

            