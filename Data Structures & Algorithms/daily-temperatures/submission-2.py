class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # holds items like (temperature, index)
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                index = stack.pop()[1]
                res[index] = i - index
            stack.append((temperatures[i], i))

        return res
                

