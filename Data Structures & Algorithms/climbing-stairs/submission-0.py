class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dp(i, stepsTaken):
            if i == n:
                return 1
            elif i > n:
                return 0
            else:
                if (i, stepsTaken) in cache:
                    return cache[(i, stepsTaken)]
                oneStep = dp(i + 1, stepsTaken + 1)
                twostepsTaken = dp(i + 2, stepsTaken + 2)
                ans = oneStep + twostepsTaken
                cache[(i, stepsTaken)] = ans
                return ans

        return dp(0, 0)
