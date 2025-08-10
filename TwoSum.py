class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for ind in range(len(nums)):
            val = nums[ind]
            inv_val = target - val
            inv_val_ind =  nums.index(inv_val) if inv_val in nums else -1

            if ind != inv_val_ind and inv_val_ind != -1:
                return [ind, inv_val_ind]
