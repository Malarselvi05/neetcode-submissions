class Solution:

    def encode(self, strs: List[str]) -> str:
       y=''
       for word in strs:
         x=str(len(word))
         y+=x+'#'+word
       return y 
         
    def decode(self, s: str) -> List[str]:
       i=0
       ans=[]
       while i<len(s):
        j=i
        while s[j]!='#':
          j+=1
        length=int(s[i:j])
        j+=1
        word = s[j : j+length]
        i = j + length
        ans.append(word)
       return ans