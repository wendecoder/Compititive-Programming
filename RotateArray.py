class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - k
        nums1 = [0] * len(nums)
        l = 0
        if k == 0:
            pass
        else:
            if k > len(nums):
                j = k % len(nums)
                j = -j
                # if k % len(nums) == 0:
                while l < len(nums):
                    nums1[i] = nums[j]
                    j += 1
                    i += 1
                    l += 1
                # else:
                #     while l < len(nums):
                #         nums1[i] = nums[j]
                #         j += 1
                #         i += 1
                #         l += 1
                    # nums1[0], nums1[len(nums) - 1] = nums1[len(nums) - 1], nums1[0]
            else:
                while l < k:
                    nums1[i] = nums[j]
                    j += 1
                    i += 1
                    l += 1
                for m in range(len(nums) - k):
                    nums1[m + k] = nums[m]

            for m in range(len(nums)):
                nums[m] = nums1[m]
