class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longestSub = 0
        stack = []
        if len(s) == 1:
            return 1
        while j < len(s):
            stack.append(s[j])
            if len(set(stack)) == len(stack):
                j += 1
                longestSub = max(longestSub, (j - i))
            else:
                while len(set(stack)) != len(stack):
                    stack.pop(0)
                    i += 1
                # if s[j] == s[j - 1]:
                #     i = j
                #     j += 1
                j += 1
        return longestSub
