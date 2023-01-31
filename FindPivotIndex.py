class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        
        for i in range(1, length):
            nums[i] = nums[i] + nums[i - 1]
        if nums[length - 1] - nums[0] == 0:
            return 0
        for i in range(1, length):
            if nums[i - 1] == nums[length - 1] - nums[i]:
                return i
        if nums[length - 2] == 0:
            return 0
        return -1
