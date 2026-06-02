class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        x=list(s)
        y=list(t)
        x.sort()
        y.sort()
        result=False
        for letter in x:
           a[letter]=a.get(letter,0)+1
        for letter in y:
            b[letter]=b.get(letter,0)+1
            
        
        result=list(a.items())==list(b.items())
    
        return result