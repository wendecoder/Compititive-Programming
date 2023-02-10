class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        
        # res = []
        # i = 0
        # j = (i + length)
        # if len(p) > len(s):
        #     return []
        # while j <= len(s):
        #     dec = Counter()
        #     for ch in p:
        #         dec[ch] += 1   
        #     for ch in s[i:j]:
        #         if ch in p:
        #             dec[ch] -= 1
        #     print(dec)
        #     if all(v == 0 for v in dec.values()):
        #         res.append(i)           
        #     i += 1
        #     j += 1
        # return res
        hm, res, pL, sL = defaultdict(int), [], len(p), len(s)
        if pL > sL: return []

        for ch in p: hm[ch] += 1

       
        for i in range(pL-1):
            if s[i] in hm: hm[s[i]] -= 1
            
        for i in range(-1, sL-pL+1):
            if i > -1 and s[i] in hm:
                hm[s[i]] += 1
            if i+pL < sL and s[i+pL] in hm: 
                hm[s[i+pL]] -= 1
                
            if all(v == 0 for v in hm.values()): 
                res.append(i+1)
                
        return res
