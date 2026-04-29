class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dp(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                if i in cache:
                    return cache[i]
                oneStep = dp(i + 1)
                twoSteps = dp(i + 2)
                ans = oneStep + twoSteps
                cache[i] = ans
                return ans

        return dp(0)

