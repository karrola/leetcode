class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        words = s.split()
        i = 0

        if len(pattern) != len(words): return False

        for letter in pattern:
            if letter not in mapping:
                mapping[letter] = words[i]
            else:
                if mapping[letter] != words[i]: return False
            i += 1

        if len(mapping.values()) != len(set(mapping.values())): return False