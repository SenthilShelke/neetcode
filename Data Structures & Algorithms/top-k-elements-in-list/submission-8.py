class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        toReturn = []
        for i in range(k):
            mostFrequent = max(count.values())
            for key in count:
                if count[key] == mostFrequent:
                    toReturn.append(key)
                    del count[key]
                    break

        return toReturn


