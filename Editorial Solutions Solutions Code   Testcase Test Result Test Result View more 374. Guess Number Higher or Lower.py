# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        return self.binaly_search(1, n) 

    def binaly_search(self, left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2

        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1: 
            return self.binaly_search(left, mid - 1) 
        else:
            return self.binaly_search(mid + 1, right)
        
