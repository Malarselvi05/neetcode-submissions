class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      a=set()
      x=False
      for num in nums:
          if num in a:
              x=True

          a.add(num)
      
      return x
      
            
            