class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        arr = [0] * (len(nums) + 1)
        for i in range(len(nums) + 1):
            arr[i] = []

        for key in count:
            value = count[key]
            arr[value].append(key)

        res = []
        for i in range(len(arr) - 1, 0, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res


# 1 -> 3
# 2 -> 1
# 3 -> 2