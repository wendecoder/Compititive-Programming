class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        prev = 0
        curr = 0
        for bit in nums:
            if bit:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0
        return longest - (longest == len(nums))
