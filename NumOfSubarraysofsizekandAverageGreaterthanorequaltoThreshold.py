class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # i = 0
        # j = (i + k)
        # res = 0
        # maxsum = sum(arr[i:j])
        # avg = maxsum / k
        # while j < len(arr):
        #     if avg >= threshold:
        #         res += 1
        #     j += 1
        #     if j < len(arr):
        #         maxsum = (maxsum - arr[i]) + arr[j]
        #         avg = (maxsum) / k
        #     i += 1
            
        # return res
        Len = 0
        Sum = 0
        ans = 0

        for i in range(0, len(arr)):

            if Len == k:

                if Sum >= threshold:
                    ans += 1

                Sum = Sum - (arr[i-k]/k)
                Len -= 1

            Sum += (arr[i]/k)
            Len += 1

        if Sum >= threshold:
            ans += 1
            
        return ans
