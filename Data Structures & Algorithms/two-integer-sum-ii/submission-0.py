class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        toReturn = []
        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in numbers:
                j = i + 1
                while numbers[j] != difference:
                    print(j)
                    j += 1
                toReturn = [i+1, j+1]
                return toReturn
            