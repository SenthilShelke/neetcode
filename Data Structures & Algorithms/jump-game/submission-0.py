class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}

        def dp(currentPos):
            if currentPos >= (len(nums) - 1):
                return True

            if currentPos in cache:
                return cache[currentPos]

            i = 1
            while i <= nums[currentPos]:
                ans = dp(currentPos + i)
                cache[currentPos] = ans
                if ans == True:
                    return True
                i += 1
            return False

        return dp(0)

            