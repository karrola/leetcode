class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        if s == "": return True

        for i in range(len(t)):
            if t[i] == s[j]: 
                if j == len(s) - 1: return True
                j += 1
    
        return False