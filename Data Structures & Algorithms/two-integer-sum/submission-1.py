class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        toReturn = []
        seen = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in seen:
                toReturn.append(i)
                toReturn.append(seen[difference])
                toReturn.sort()
                return toReturn
            seen[nums[i]] = i