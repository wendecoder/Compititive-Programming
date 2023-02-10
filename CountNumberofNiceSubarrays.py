class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        odd_counts,res = 0,0
        hmap[0] = 1
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                odd_counts+=1
            res += hmap[odd_counts-k]
            hmap[odd_counts]+=1
        return res
