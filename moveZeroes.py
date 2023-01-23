class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[non_zero] = nums[non_zero], nums[j]
                non_zero = non_zero + 1
