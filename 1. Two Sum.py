class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {} # キー: numsのval, val: numsのidex
        for i in range(len(nums)):
            x = target - nums[i] # これが存在するかどうか
            if x in hash:
                return [hash[x], i]

            hash[nums[i]] = i

        
