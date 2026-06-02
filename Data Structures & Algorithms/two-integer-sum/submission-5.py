class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #arrays check all the elements.
        
        z={}
        for i,num in enumerate(nums):
            need=target-num
            if need in z:
                return[z[need],i]
            z[num]=i
 
        return list(z)   