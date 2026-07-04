class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = s.lower()
        t1 = t.lower()
        
        s2 = s1.replace(" ", "")
        s3 = t1.replace(" ", "")
        if sorted(s2)==sorted(s3):
            return True
        else:
            return False