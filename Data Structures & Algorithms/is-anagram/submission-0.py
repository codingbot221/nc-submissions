class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s.lower())
        b=list(t.lower())
        if len(a)==len(b):
            a.sort()
            b.sort()
            if a==b:
               return  True
        return False