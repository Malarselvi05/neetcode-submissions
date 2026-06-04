class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum=0
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                sum=numbers[i]+numbers[j]
                if sum==target:
                    x=[]
                    x.append(i+1)
                    x.append(j+1)
                    x.sort()
                    break
        return x           