class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        jumps = 0
        while i + nums[i] < len(nums) - 1:
            maxJump = i + 1 + nums[i + 1]
            for j in range(i + 1, i + nums[i] + 1):
                maxJump = max(maxJump, j + nums[j])
            j = i + 1
            while nums[j] + j != maxJump:
                j += 1
            i = j
            jumps += 1

        return jumps + 1
