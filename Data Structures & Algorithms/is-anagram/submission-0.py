class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1=[]
        arr2=[]
        for char in s:
            arr1.append(char)
        for char in t:
            arr2.append(char)
        arr1.sort()
        arr2.sort()
        if arr1==arr2:
            return True
        else:
            return False