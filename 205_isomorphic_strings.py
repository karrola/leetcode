class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        i = 0
        for letter in s:
            if letter not in mapping: 
                mapping[letter] = t[i]
            elif letter in mapping:
                if mapping[letter] != t[i]: return False
            i += 1
        if len(mapping.values()) != len(set(mapping.values())): return False
        return True