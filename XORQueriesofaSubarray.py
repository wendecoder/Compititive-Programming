class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefix_or = [arr[0]]
        for i in range(1, len(arr)):
            prefix_or.append(prefix_or[i-1] ^ arr[i])
        ans = []
        for L, R in queries:
            L_one_less = None
            if(L == 0):
                ans.append(prefix_or[R])
                continue
            L_one_less = prefix_or[L-1]
            sub_res = prefix_or[R]
            res = L_one_less ^ sub_res
            ans.append(res)
        return ans
