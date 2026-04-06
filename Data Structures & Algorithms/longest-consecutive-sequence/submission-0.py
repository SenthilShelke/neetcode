class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0
        for i in range(len(nums)):
            if nums[i] - 1 in seen:
                continue
            else:
                seen.add(nums[i])
                j = 1
                while(True):
                    if nums[i] + j in nums:
                        j += 1
                        continue
                    else:
                        break
                if j > longest:
                    longest = j

        return longest


