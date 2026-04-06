class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in map:
                toReturn = [i, map[difference]]
                return sorted(toReturn)
            map[nums[i]] = i