class Solution:
    def isHappy(self, n: int) -> bool:
        results = []
        while True:
            res = 0
            digits = [int(d) for d in str(n)]
            for digit in digits:
                res += digit**2
            
            if res == 1: return True
            if res in results: return False

            results.append(res)
            n = res