class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        arr = []

        for key in count:
            arr.append(key)

        arr = sorted(arr)

        lengths = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if j + 1 == len(arr):
                    break
                elif (arr[j + 1] != (arr[j] + 1)):
                    break
                lengths.append(j - i + 1)

        if len(lengths) == 0:
            return 1

        return max(lengths) + 1

# -1: 2
# 0: 1
# 1: 1
# 3: 1
# 4: 1
# 5: 1
# 6: 1
# 7: 1
# 8: 1
# 9: 1
