class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        helperSet = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j], nums[k]) not in helperSet:
                        helperSet.add((nums[i], nums[j], nums[k]))
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1
                    else:
                        j += 1


                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

        return res

-4, -1, -1, 0, 1, 2