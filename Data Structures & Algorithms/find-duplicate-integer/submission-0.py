class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # method: negative marking
        # every number corresponds to an index
        for i, num in enumerate(nums):
            # go the index 'num'. Is always valid since
            # num is between [1,n]
            # if num < 0:
            #     return i
            check = num
            if num < 0:
                check = -num
                # this means that the 'index i' has already
                # occured in the array
            val = nums[check]
            if val < 0:
                return check
            nums[check] = -1*val
        return -1