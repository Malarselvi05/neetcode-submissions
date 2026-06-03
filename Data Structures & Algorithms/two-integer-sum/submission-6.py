class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #arrays check all the elements.
        
        z={}
        for index,num in enumerate(nums):
            need=target-num
            if need in z:
                return [z[need],index]
            z[num]=index
        return list(z)