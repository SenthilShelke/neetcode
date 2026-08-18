class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        arr = []
        for i in range(len(nums) + 1):
            arr.append([])

        for key in count:
            freq = count[key]
            arr[freq].append(key)
                
        res = []

        for i in range(len(nums), 0, -1):
            for j in range(len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res
                    

