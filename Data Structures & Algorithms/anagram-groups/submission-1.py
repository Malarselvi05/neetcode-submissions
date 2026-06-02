class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we have a list,the idea will be finding the words which have 
        # same words and group them as a sublist.
        dict_count={}
        a=[]

        for word in strs:
            key=''.join(sorted(word))
            if key not in dict_count:
                dict_count[key]=[]
                dict_count[key].append(word)
            else:
                dict_count[key].append(word)
        for value in dict_count.values():
            a.append(value)
        return a
        
            