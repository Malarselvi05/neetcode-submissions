class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we have a list,the idea will be finding the words which have 
        # same words and group them as a sublist.
        dixt={}
        a=[]
        for word in strs:
            key="".join(sorted(word))
            if key not in dixt:
                dixt[key]=[]
                dixt[key].append(word)
            else:
                dixt[key].append(word)
        for value in dixt.values():
            a.append(value)
        return a
            