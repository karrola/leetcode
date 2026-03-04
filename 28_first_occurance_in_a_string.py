def strStr(haystack: str, needle: str) -> int:
    i = 0
    while i <= (len(haystack) - len(needle)):
        if haystack[i] == needle[0]: 
            for j in range(1, len(needle)):
                if haystack[i + j] != needle[j]: 
                    i += j
                    break
                elif j == len(needle) - 1: return i
        i += 1
    return -1

print(strStr("hello", "ll"))