# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # nは1スタート
        return self.binaly_search(1, n)
        

    def binaly_search(self, left, right):
        if left > right:  
            return left

        mid = (left + right) // 2 

        if isBadVersion(mid):
            # 右にtrueのバージョンがあるかもしれない
            return self.binaly_search(left, mid-1)
        else:
            # 左にfalseのバージョンがあるかもしれない
            return self.binaly_search(mid+1 , right)

