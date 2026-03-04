class Solution:
    def longestCommonPrefix(self, strs) -> str:
        sorted_strs = sorted(strs)
        first = sorted_strs[0]
        last = sorted_strs[-1]
        prefix = ""

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]: prefix += first[i]
            else: return prefix

        return prefix