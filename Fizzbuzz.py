class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(0, n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                answer.insert(i, "FizzBuzz")
            elif (i + 1) % 3 == 0:
                answer.insert(i, "Fizz")
            elif (i + 1) % 5 == 0:
                answer.insert(i, "Buzz")
            else:
                answer.insert(i, str(i + 1))
        return answer
