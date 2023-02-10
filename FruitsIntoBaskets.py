class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # i = 0
        # j = 0 
        # stack = []
        # maximum = 0
        # count = 0
        # while j < len(fruits):
        #     stack.append(fruits[j])
        #     if len(set(stack)) <= 2:
        #         j += 1
        #         maximum = max(maximum, (j - i))
        #     else:
        #         stack.pop(0)
        #         i += 1
        #     count += 1
        # return maximum
        basket = {}
        left = 0
        
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        return right - left + 1
