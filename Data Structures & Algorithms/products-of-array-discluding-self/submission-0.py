class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
       left=[1]*len(nums)
       right=[1]*len(nums)
       output=[]
       for i in range(1,len(nums)):
         left[i]=left[i-1]*nums[i-1]
       for i in reversed(range(len(nums)-1)):
          right[i]=right[i+1]*nums[i+1]
    
       for i in range(len(nums)):
          x=left[i]*right[i]
          output.append(x)
       return(output)