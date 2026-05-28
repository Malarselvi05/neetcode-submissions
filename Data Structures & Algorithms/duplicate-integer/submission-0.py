class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=list()
        count=0
        for i in range(len(nums)):
            a.append(nums[i])
            if a.count(nums[i])!=1:
                return True
                break
        return False
            
            