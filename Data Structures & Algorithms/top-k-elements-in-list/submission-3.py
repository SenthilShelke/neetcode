class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        arr = [[] for i in range(len(nums) + 1)]
        for key in count:
            arr[count[key]].append(key)

        toReturn = []

        for i in range(len(arr) - 1, 0, -1):
            for j in range(len(arr[i])):
                if(len(arr[i]) == 0):
                    break
                else:
                    toReturn.append(arr[i][j])
                    if len(toReturn) == k:
                        return toReturn
    

        
             


