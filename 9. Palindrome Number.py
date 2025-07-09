class Solution:
    def isPalindrome(self, x: int) -> bool:
        ls = list(str(x))
        
        for n in range(0, len(ls) - 1): # 配列は0始まりのため
            if ls[n] != ls[len(ls) - n - 1]:　# 配列は0始まりのため
                return False
        return True
