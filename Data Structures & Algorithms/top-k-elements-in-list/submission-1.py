class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we have given with a list of numbers, find the frequency of
        #them and return the key if the value is greater than or equal
        #to k.
        dict_count={}
        a=[]
        for num in nums:
            
            if num in dict_count:
                dict_count[num]+=1
            else:
                dict_count[num]=1
        sorted_items=(sorted(dict_count.items(), key=lambda x:x[1], reverse=True))
        for i in range(k):
            a.append(sorted_items[i][0])
        return a
        
