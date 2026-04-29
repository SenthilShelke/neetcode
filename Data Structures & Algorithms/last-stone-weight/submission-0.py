class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if x == y:
                continue
            elif x < y:
                stones.append(y - x)

        if len(stones) == 0:
            return 0
        else:
            return stones[0]