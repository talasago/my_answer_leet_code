class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # lenはインデックスの個数を返す。インデックスは0始まり。インデックスの場所を指定するために-1している
        return self.binaly_search(nums, target, 0, len(nums) - 1) 

    def binaly_search(self, nums, target, left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.binaly_search(nums, target, left, mid - 1) 
        else: # target > nums[mid]:
            return self.binaly_search(nums, target,mid + 1, right)
