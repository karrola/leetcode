class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        ransomnote_dict = {}
        for letter in magazine:
            if letter not in magazine_dict: magazine_dict[letter] = 1
            else: magazine_dict[letter] += 1
        for letter in ransomNote:
            if letter not in ransomnote_dict: ransomnote_dict[letter] = 1
            else: ransomnote_dict[letter] += 1
        for key in ransomnote_dict:
            if key not in magazine_dict or ransomnote_dict[key] > magazine_dict[key]:
                return False
        return True