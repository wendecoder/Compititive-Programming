class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        newarray = [0] * length
        for i in range(length):
            for j in range(length):
                if nums[i] > nums[j]:
                    newarray[i] += 1
        return newarray
