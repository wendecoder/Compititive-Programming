class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxcount = 0
        given_k = k
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            else:
                if given_k > 0:
                    r += 1
                    given_k -= 1
                else:
                    maxcount = max(maxcount, (r - l))
                    if k != 0:
                        while l < r:
                            if nums[l] == 0:
                                given_k += 1
                                l += 1
                                break
                            l += 1
                    else:
                        r += 1
                        l = r
        maxcount = max(maxcount, (r - l))
        return maxcount
