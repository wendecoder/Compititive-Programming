class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        new_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for i in range(k):
            if new_list[i] in vowels:
                count = count + 1
        max_num = count
        for end in range(k,len(s)):
            start = end - k + 1
            if new_list[start-1] in vowels:
                count = count - 1
            if new_list[end] in vowels:
                count = count + 1
            max_num = max(max_num, count)

        return max_num  
