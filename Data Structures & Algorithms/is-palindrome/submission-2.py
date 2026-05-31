class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=[]
        for word in s:
            if word.isspace():
                continue
            if word.isalnum():
                x.append(word.lower())
        t=x[::-1]
        if t==x:
            return True
        else:
            return False