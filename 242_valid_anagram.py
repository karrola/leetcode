class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dict_s = {}
        dict_t = {}

        for letter in s:
            if letter not in dict_s: dict_s[letter] = 1
            else: dict_s[letter] += 1

        for letter in t:
            if letter not in dict_t: dict_t[letter] = 1
            else: dict_t[letter] += 1

        for key in dict_s:
            if key not in dict_t or dict_s[key] != dict_t[key]: return False
        
        return True