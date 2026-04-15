class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # method: negative marking
        # every number corresponds to an index
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] *= -1
        return -1