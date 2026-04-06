class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        res = []
        for i in range(k):
            mostFrequent = max(count.values())
            for key in count:
                if mostFrequent == count[key]:
                    res.append(key)
                    del count[key]
                    break

        return res


